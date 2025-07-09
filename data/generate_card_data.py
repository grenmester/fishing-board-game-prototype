"""Generate card data for fishing board game and save it to the server."""

import math
import sys

import pandas as pd
import yaml


with open("data.yaml", "r", encoding="utf-8") as stream:
    try:
        data = yaml.safe_load(stream)
    except yaml.YAMLError as e:
        print(e)
        sys.exit(1)

card_df = pd.DataFrame(data["cardData"])
card_df["adjustedOdds"] = card_df["odds"] * 6 ** (4 - card_df["numDice"]) // 6
card_df["adjustedOdds"] = card_df["adjustedOdds"].apply(lambda x: round(x / 2.16, 2))
card_df["money"] = (
    card_df["adjustedOdds"].apply(lambda x: math.floor(math.log2(360 / x)))
    + card_df["numDice"]
)

coast_card_df = card_df[card_df["numDice"] <= 3]
ocean_card_df = card_df[card_df["numDice"] >= 3]
river_card_df = card_df[card_df["numDice"] <= 2]

fish_df = pd.DataFrame(data["fishData"])

coast_fish_df = fish_df[fish_df["habitat"] == "coast"].reset_index(drop=True)
ocean_fish_df = fish_df[fish_df["habitat"] == "ocean"].reset_index(drop=True)
river_fish_df = fish_df[fish_df["habitat"] == "river"].reset_index(drop=True)

coast_card_df = coast_card_df.sample(n=len(coast_fish_df), replace=True).reset_index(
    drop=True
)
ocean_card_df = ocean_card_df.sample(n=len(ocean_fish_df), replace=True).reset_index(
    drop=True
)
river_card_df = river_card_df.sample(n=len(river_fish_df), replace=True).reset_index(
    drop=True
)

coast_df = coast_fish_df.join(coast_card_df, how="inner")
ocean_df = ocean_fish_df.join(ocean_card_df, how="inner")
river_df = river_fish_df.join(river_card_df, how="inner")

df = pd.concat([coast_df, ocean_df, river_df])

with open("merged_output.yaml", "w", encoding="utf-8") as file:
    data = df.drop(
        columns=["numDice", "odds", "adjustedOdds", "scientificName"]
    ).to_dict(orient="records")
    yaml.dump({"fish": data}, file, sort_keys=False, indent=2)
