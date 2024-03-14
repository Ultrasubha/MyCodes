# Q.5) Number of matches played per year for all the years in IPL

import csv
import matplotlib.pyplot as plt


def calculate():
    with open("matches.csv", "r") as matches:
        matches_per_year = {}

        for match in csv.DictReader(matches):
            year = match['season']
            # Count matches per year
            matches_per_year[year] = matches_per_year.get(year, 0) + 1

    years = list(matches_per_year.keys())
    matches_count = list(matches_per_year.values())
    return years, matches_count


def plot(years, matches_count):
    # Plotting
    plt.figure(figsize=(10, 6))
    plt.bar(years, matches_count, color='skyblue')
    plt.title('Number of Matches Played per Year in IPL')
    plt.xlabel('Year')
    plt.ylabel('Number of Matches')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()


def execute():
    years, matches_count = calculate()
    plot(years, matches_count)


execute()
