"""
explore.py
Explore the World Cup data before answering the questions:
check for missing values, data types, team names, results, and goals.
"""

import pandas as pd


def print_title(title):
    """Print a section title so the output is easy to read."""
    print()
    print("=" * 50)
    print(title)
    print("=" * 50)


# Load the CSV file into a DataFrame and keep only World Cup matches (filter).
# .copy() makes a separate table, so we can safely add new columns to it.
matches = pd.read_csv("results.csv")
world_cup = matches[matches["tournament"] == "FIFA World Cup"].copy()
print("World Cup matches:", len(world_cup))

# 1. Missing values: a match with no score would break the analysis
print_title("1. Missing values in each column")
print(world_cup.isna().sum())

# 2. Data types: the scores must be numbers, but the date is plain text
print_title("2. Data type of each column")
print(world_cup.dtypes)

# Data conversion: turn the date text into a real date, then get the year
world_cup["date"] = pd.to_datetime(world_cup["date"])
world_cup["year"] = world_cup["date"].dt.year

# 3. How many matches each World Cup had (the tournament grew over time)
print_title("3. Matches per World Cup")
print(world_cup["year"].value_counts().sort_index())

# 4. Team names: a team can be the home or the away team, so look at both columns
print_title("4. Teams that have played in a World Cup")
teams = pd.concat([world_cup["home_team"], world_cup["away_team"]]).unique()
print("Number of teams:", len(teams))
print(sorted(teams))

# 5. Results: count home wins, away wins, and draws
print_title("5. Match results")
home_wins = (world_cup["home_score"] > world_cup["away_score"]).sum()
away_wins = (world_cup["away_score"] > world_cup["home_score"]).sum()
draws = (world_cup["home_score"] == world_cup["away_score"]).sum()
print("Home team won:", home_wins)
print("Away team won:", away_wins)
print("Draws:", draws)

# 6. Goals: add a new column with the total goals in each match
print_title("6. Goals per match")
world_cup["total_goals"] = world_cup["home_score"] + world_cup["away_score"]
print("Average goals per match:", round(world_cup["total_goals"].mean(), 2))
print("Most goals in one match:", world_cup["total_goals"].max())
highest = world_cup.loc[world_cup["total_goals"].idxmax()]
print(f"Highest-scoring match: {highest['home_team']} {highest['home_score']} - "
      f"{highest['away_score']} {highest['away_team']} ({highest['year']})")