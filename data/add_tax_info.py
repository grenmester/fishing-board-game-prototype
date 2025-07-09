"""Add scientificFamily and scientificOrder to fish data from GBIF API."""

import sys
from pathlib import Path

import requests
import yaml
from tqdm import tqdm


def fetch_taxonomic_info(scientific_name):
    """Fetch taxonomic information (family and order) from GBIF API."""
    try:
        url = (
            f"https://api.gbif.org/v1/species/match?name={scientific_name}&rank=species"
        )
        response = requests.get(url)
        response.raise_for_status()  # Raise exception for bad status codes
        data = response.json()
        return {"family": data.get("family"), "order": data.get("order")}
    except requests.exceptions.RequestException as e:
        print(f"Error fetching taxonomic info for {scientific_name}: {e}")
        return None


def update_fish_data(input_path, output_path):
    """Update fish data with scientificFamily and scientificOrder."""
    with open(input_path, "r", encoding="utf-8") as file:
        data = yaml.safe_load(file)

    fish_list = data.get("fishData", [])

    for fish in tqdm(fish_list):
        # Only make API call if either field is missing
        if "scientificFamily" not in fish or "scientificOrder" not in fish:
            tax_info = fetch_taxonomic_info(fish["scientificName"])
            if tax_info:
                if "scientificFamily" not in fish and tax_info["family"]:
                    fish["scientificFamily"] = tax_info["family"]
                if "scientificOrder" not in fish and tax_info["order"]:
                    fish["scientificOrder"] = tax_info["order"]

    with open(output_path, "w", encoding="utf-8") as file:
        yaml.dump(data, file, sort_keys=False, default_flow_style=False)

    print(f"Updated YAML written to: {output_path}")


if __name__ == "__main__":
    data_path = Path("data.yaml")
    updated_data_path = Path("fish_tax_data.yaml")

    if not data_path.exists():
        print("Error: 'data.yaml' not found in the current directory.")
        sys.exit(1)

    update_fish_data(data_path, updated_data_path)
