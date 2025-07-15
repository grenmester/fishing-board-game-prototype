"""Extract fish information using local LLM inference"""

from pathlib import Path
from typing import List, Optional

import requests
import yaml
from bs4 import BeautifulSoup
from langchain_core.callbacks import StreamingStdOutCallbackHandler
from langchain_core.prompts import PromptTemplate
from langchain_ollama.chat_models import ChatOllama
from pydantic import BaseModel, Field
from tqdm import tqdm

STREAM_LLM_OUTPUT = False
INPUT_FILE = "data.yaml"
OUTPUT_FILE = "fish_properties.yaml"
PROCESSING_LIMIT = 50

EXTRACTION_PROMPT = PromptTemplate.from_template("""
You are a marine biology expert in California fish species. From the text below, extract information for the fish specified.

FISH: {scientific_name}

TEXT:
{content}

Based on the text, provide a structured JSON output with the following fields:
- colors: The primary color of the fish, or a list of colors and coloration patterns if the fish has more than one color.
- size_range: The size range in cm (e.g., '20-30 cm') of an adult species.
- confidence: A score from 0.0 to 1.0 indicating your confidence in the extracted information.
- additional_notes: Any other relevant information.

Rules:
- Only extract information that is clearly stated in the text.
- Convert inches to cm (1 inch = 2.54 cm).
- If a field is not mentioned in the text, leave it as null or an empty list.
""")

COMBINATION_PROMPT = PromptTemplate.from_template("""
You are a marine biology expert in California fish species. Combine the information from the JSON sources below into a single, comprehensive record for the specified fish.

FISH: {scientific_name}

SOURCES:
{sources}

Create a new JSON object with the following fields, taking the best information from all sources:
- colors: A combined list of unique colors. (e.g. ['silver', 'blue line in the middle of the body'])
- size_range: The most accurate or comprehensive size range. (e.g. '20-30 cm' or 'up to 50 cm')
- confidence: A new confidence score (0.0-1.0) based on the agreement between sources.
- additional_notes: Combined notes, mentioning any conflicts between the sources.

Rules:
- Merge lists and remove duplicates.
- If sources conflict, choose the more specific information and mention the conflict in the notes.
- If sources agree, the new confidence score should be higher. If they conflict, it should be lower.
""")


class FishProperties(BaseModel):
    """Structured output for fish information"""

    colors: List[str] = Field(default=[], description="Colors and coloration patterns of the fish")
    size_range: Optional[str] = Field(
        default=None, description="Size range in cm or inches (e.g., '20-30 cm' or 'up to 50 cm')"
    )
    confidence: float = Field(
        description="Confidence level (0-1) in the extracted information",
        ge=0.0,
        le=1.0,
    )
    additional_notes: Optional[str] = Field(default=None, description="Any additional relevant information")
    sources_used: List[str] = Field(default=[], description="List of sources successfully used to extract information")


def load_fish_data() -> tuple[List[tuple[str, str]], List[dict]]:
    """Load fish data and existing extracted data."""
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        fish_data = yaml.safe_load(f)
    fish_list = [(fish["name"], fish["scientificName"]) for fish in fish_data["fishData"]]

    output_path = Path(OUTPUT_FILE)
    existing_data = []
    if output_path.exists():
        with open(output_path, "r", encoding="utf-8") as f:
            existing_data = yaml.safe_load(f) or []

    return fish_list, existing_data


def get_page_content(session, url: str, max_length: int = 4000) -> Optional[str]:
    """Fetch and clean page content"""
    try:
        response = session.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, "html.parser")
        for script in soup(["script", "style", "nav", "header", "footer", "aside"]):
            script.decompose()
        text = " ".join(soup.stripped_strings)

        return text[:max_length]
    except Exception as e:
        tqdm.write(f"❌ Error scraping {url}: {e}")
        return None


def extract_fish_info(structured_llm, content: str, scientific_name: str, source: str) -> Optional[FishProperties]:
    """Extract fish info"""
    try:
        chain = EXTRACTION_PROMPT | structured_llm
        fish_info = chain.invoke({"content": content, "scientific_name": scientific_name})
        fish_info.additional_notes = f"Source: {source}. {fish_info.additional_notes or ''}"
        fish_info.sources_used = [source]
        return fish_info
    except Exception as e:
        tqdm.write(f"❌ Error extracting info with LLM: {e}")
        return None


def search_source(
    session,
    structured_llm,
    source_name: str,
    search_url_template: str,
    name: str,
    scientific_name: str,
) -> Optional[FishProperties]:
    """Search a source for fish information"""
    try:
        if source_name == "NOAA":
            search_url = search_url_template.format(name=name.lower().replace(" ", "-"))
        elif source_name == "FishBase":
            search_url = search_url_template.format(scientific_name=scientific_name.replace(" ", "-"))
        elif source_name == "Wikipedia":
            search_url = search_url_template.format(scientific_name=scientific_name.replace(" ", "_"))
        else:
            search_url = search_url_template.format(scientific_name=scientific_name)

        content = get_page_content(session, search_url)

        if content:
            return extract_fish_info(structured_llm, content, scientific_name, source_name)
        return None

    except Exception as e:
        tqdm.write(f"❌ Error searching {source_name}: {e}")
        return None


def combine_results(structured_llm, results: List[FishProperties], scientific_name: str) -> FishProperties:
    """Combine multiple results using local LLM"""
    if not results:
        return FishProperties(
            confidence=0.0,
            additional_notes="No information found from available sources.",
        )

    if len(results) == 1:
        return results[0]

    try:
        chain = COMBINATION_PROMPT | structured_llm
        sources_json = [r.model_dump_json() for r in results]
        combined_info = chain.invoke(
            {
                "scientific_name": scientific_name,
                "sources": sources_json,
            }
        )

        all_sources_used = set()
        for r in results:
            all_sources_used.update(r.sources_used)
        combined_info.sources_used = sorted(list(all_sources_used))

        return combined_info

    except Exception as e:
        tqdm.write(f"❌ Error combining results: {e}")
        best_result = max(results, key=lambda x: x.confidence)
        return best_result


def get_fish_info(session, structured_llm, name: str, scientific_name: str) -> FishProperties:
    """Main method to get fish information from multiple sources"""
    results = []

    sources = [
        {
            "name": "NOAA",
            "url_template": "https://www.fisheries.noaa.gov/species/{name}",
        },
        {
            "name": "FishBase",
            "url_template": "https://www.fishbase.se/summary/{scientific_name}.html",
        },
        {
            "name": "Wikipedia",
            "url_template": "https://en.wikipedia.org/wiki/{scientific_name}",
        },
    ]

    for source in sources:
        tqdm.write(f"📊 Searching {source['name']}...")
        info = search_source(
            session,
            structured_llm,
            source["name"],
            source["url_template"],
            name,
            scientific_name,
        )
        if info:
            results.append(info)

    return combine_results(structured_llm, results, scientific_name)


def main() -> None:
    """Extract fish information using local LLM inference"""
    llm = ChatOllama(
        model="gemma3:latest",
        callbacks=[StreamingStdOutCallbackHandler()] if STREAM_LLM_OUTPUT else [],
        temperature=0.1,
        num_predict=1024,
    )
    structured_llm = llm.with_structured_output(FishProperties)
    session = requests.Session()

    fish_list, existing_data = load_fish_data()
    existing_names = {item["name"] for item in existing_data}

    processing_list = []
    for name, scientific_name in fish_list:
        if name not in existing_names:
            processing_list.append((name, scientific_name))
        if len(processing_list) >= PROCESSING_LIMIT:
            break

    for name, scientific_name in tqdm(processing_list, desc="Processing Fish"):
        try:
            tqdm.write(f"🐟 Searching for information about: {name} ({scientific_name})")

            fish_info = get_fish_info(session, structured_llm, name, scientific_name)

            fish_output = {"name": name, "scientific_name": scientific_name}
            fish_output.update(fish_info.model_dump())

            existing_data.append(fish_output)
            with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
                yaml.safe_dump(existing_data, f, allow_unicode=True, sort_keys=False)

            tqdm.write(f"✨ Successfully fetched and saved data for {scientific_name}")
        except Exception as e:
            tqdm.write(f"❌ Error processing {scientific_name}: {e}")


if __name__ == "__main__":
    main()
