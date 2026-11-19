"""
explore.py
First look at the dataset: make sure Pandas can read it.
"""

import pandas as pd

# Load the CSV file into a DataFrame (a table)
matches = pd.read_csv("results.csv")

print("Total matches in the file:", len(matches))
print("Columns:", list(matches.columns))
print()
print("First 5 rows:")
print(matches.head())

# Keep only World Cup matches (this is a filter)
world_cup = matches[matches["tournament"] == "FIFA World Cup"]
print()
print("World Cup matches:", len(world_cup))
print("First World Cup match:", world_cup["date"].min())
print("Last World Cup match:", world_cup["date"].max())