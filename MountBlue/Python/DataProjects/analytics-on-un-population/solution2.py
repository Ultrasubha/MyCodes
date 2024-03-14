# 2: For the year 2014. Bar Chart of population of ASEAN countries
import csv
import matplotlib.pyplot as plt


asian_countries = ['Brunei Darussalam', 'Cambodia', 'Indonesia', "Lao People's Democratic Republic", 'Malaysia', 'Myanmar', 'Philippines', 'Singapore', 'Thailand', 'Viet Nam']
YEAR = '2014'


def calculate():
    population_by_country = {}
    with open('population-estimates_csv.csv', 'r', encoding="utf8") as csvfile:
        population_reader = csv.DictReader(csvfile)
        for population in population_reader:
            year = population['Year']
            if year == YEAR:
                region = population['Region']
                if region in asian_countries:
                    population_by_country[region] = int(
                        float(population['Population']))
    return population_by_country


def plot(population_by_country):
    regions = population_by_country.keys()
    populations = population_by_country.values()

    plt.figure(figsize=(20, 8))
    plt.bar_label(plt.bar(regions, populations), padding=5)
    plt.bar(regions, populations, color='#963e5e', tick_label = asian_countries, width=0.8)
    plt.xlabel('Region')
    plt.ylabel('Population')
    plt.title('Population of ASEAN countries in 2014')
    plt.xticks(fontsize=8)
    plt.show()


def execute():
    population_by_country = calculate()
    plot(population_by_country)


execute()
