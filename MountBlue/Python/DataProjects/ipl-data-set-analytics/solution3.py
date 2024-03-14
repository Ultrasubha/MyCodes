# Q3) Foreign umpire analysis

import csv
import matplotlib.pyplot as plt


def calculate():
    with open("umpires.csv", "r") as umpires:
        ump_data = [umpire for umpire in csv.DictReader(umpires)
                    if umpire[' country'].strip() != 'India']
    country_counts = {}

    for umpire in ump_data:
        country = umpire[' country'].strip()
        country_counts[country] = country_counts.get(country, 0) + 1

    countries = list(country_counts.keys())
    counts = list(country_counts.values())
    return countries, counts


def plot(countries, counts):
    # Plotting
    plt.figure(figsize=(10, 5))
    plt.xticks(rotation=45, ha='right')
    plt.bar(countries, counts)
    plt.xlabel("Country")
    plt.ylabel("Number of Umpire")
    plt.title("Foreign umpire analysis")
    plt.tight_layout()
    plt.show()


def execute():
    countries, counts = calculate()
    plot(countries, counts)


execute()
