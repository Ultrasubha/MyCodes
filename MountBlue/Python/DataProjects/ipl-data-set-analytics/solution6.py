# Q.6) Number of matches won per team per year in IPL

import csv
import matplotlib.pyplot as plt
from collections import defaultdict


def calculate():
    with open("matches.csv", "r") as matches:
        matches_won_per_team_per_year = defaultdict(lambda: defaultdict(int))

        for match in csv.DictReader(matches):
            year = match['season']
            winner = match['winner']
            # Count matches won per team per year
            matches_won_per_team_per_year[year][winner] += 1

    matches_won_per_team_per_year = dict(matches_won_per_team_per_year)
    teams = set(team for year_data in matches_won_per_team_per_year.values()
                for team in year_data.keys())
    years = sorted(matches_won_per_team_per_year.keys())

    return teams, years, matches_won_per_team_per_year


def plot(teams, years, matches_won_per_team_per_year):
    # Plotting
    plt.figure(figsize=(12, 8))
    bottom = None

    for team in teams:
        team_wins = [matches_won_per_team_per_year[year].get(team, 0)
                     for year in years]
        plt.bar(years, team_wins, bottom=bottom, label=team)
        if bottom is None:
            bottom = team_wins
        else:
            bottom = [sum(x) for x in zip(bottom, team_wins)]

    plt.title('Number of Matches Won per Team per Year in IPL')
    plt.xlabel('Year')
    plt.ylabel('Number of Matches Won')
    plt.legend(title='Team', bbox_to_anchor=(1, 1), loc='upper left')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()


def execute():
    teams, years, matches_won_per_team_per_year = calculate()
    plot(teams, years, matches_won_per_team_per_year)


execute()
