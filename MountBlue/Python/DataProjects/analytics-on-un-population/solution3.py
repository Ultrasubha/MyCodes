# 3: Over the years, TOTAL population of SAARC countries
import csv
import matplotlib.pyplot as plt

saarc_countries = ['Afghanistan', 'Bangladesh', 'Bhutan', 'India', 'Maldives', 'Nepal', 'Pakistan', 'Sri Lanka']


def calculate():
    population_by_year = {}
    with open('population-estimates_csv.csv', 'r', encoding="utf8") as csvfile:
        population_reader = csv.DictReader(csvfile)
        for population in population_reader:
            if population['Region'] in saarc_countries:
                year = population['Year']
                region_population = int(float(population['Population']))
                if year not in population_by_year:
                    population_by_year[year] = 0
                population_by_year[year] += region_population
    return population_by_year


def plot(population_by_year):
    years = population_by_year.keys()
    populations = population_by_year.values()

    axes = plt.subplots(figsize=(18, 9))[1]
    axes.bar(years, populations, color='#00ff00')
    axes.set_title('Population of SAARC countries Over the Years')
    axes.set_xlabel('Year')
    axes.set_ylabel('Population (in millions)')

    plt.xticks(fontsize=8, rotation=45)
    plt.yticks(fontsize=8)
    plt.show()


def execute():
    population_by_year = calculate()
    plot(population_by_year)


execute()
