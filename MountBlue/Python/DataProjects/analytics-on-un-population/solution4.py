# 4. Grouped Bar Chart - ASEAN population vs. years

import csv
import matplotlib.pyplot as plt

asian_countries = ['Brunei Darussalam', 'Cambodia', 'Indonesia', "Lao People's Democratic Republic",
                   'Malaysia', 'Myanmar', 'Philippines', 'Singapore', 'Thailand', 'Viet Nam']
START_YEAR = 2004
END_YEAR = 2014


def calculate():
    population_by_region_by_year = {}
    with open('population-estimates_csv.csv', 'r', encoding="utf8") as csvfile:
        population_reader = csv.DictReader(csvfile)
        for population in population_reader:
            region = population['Region']
            if region in asian_countries:
                year = int(population['Year'])
                if year in range(START_YEAR, END_YEAR+1):
                    region_population = int(float(population['Population']))
                    if region not in population_by_region_by_year:
                        population_by_region_by_year[region] = {}
                    population_by_region_by_year[region][year] = region_population
    return population_by_region_by_year


def plot(population_by_region_by_year):
    plt.figure(figsize=(12, 6))
    width = 0.10
    k = -5
    width_list = [i for i in range(0, 11)]
    for keys in population_by_region_by_year:
        data = list(population_by_region_by_year[keys].values())
        print(data)
        plt.bar([i + k*width for i in range(11)], data, width)
        k += 1
    years = [year for year in range(START_YEAR, END_YEAR+1)]

    plt.xlabel('Years')
    plt.ylabel('ASEAN Population')
    plt.title('Grouped Bar Chart - ASEAN population vs. years')
    plt.xticks(width_list, years, fontsize=8)
    plt.legend(asian_countries, bbox_to_anchor=(1, 1), loc="upper left")
    plt.show()


def execute():
    population_by_region_by_year = calculate()
    plot(population_by_region_by_year)


execute()
