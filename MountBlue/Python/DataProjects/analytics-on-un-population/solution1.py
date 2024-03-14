# Make a Bar Plot of 'population of India' vs. years.

import csv
import matplotlib.pyplot as plt


def calculate():
    years = []
    populations = []
    with open('population-estimates_csv.csv', 'r', encoding="utf8") as csvfile:
        population_reader = csv.DictReader(csvfile)
        for population in population_reader:
            region = population['Region']
            if region == 'India':
                years.append(population['Year'])
                populations.append(int(float(population['Population'])))
    return years, populations


def plot(years, populations):
    plt.figure(figsize=(25, 8))
    plt.bar(years, populations, color='#28acd1')
    plt.title('Population of India Over the Years')
    plt.xlabel('Year')
    plt.ylabel('Population (in millions)')
    plt.xticks(fontsize=8, rotation=45)
    plt.yticks(fontsize=8)
    plt.show()


def execute():
    years, populations = calculate()
    plot(years, populations)


execute()
