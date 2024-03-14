# 2. Bar Plot of company registration by year

import csv
import matplotlib.pyplot as plt


def process_csv_data(filename='Maharashtra.csv'):
    with open(filename, encoding='unicode_escape') as corporateData:
        header = next(corporateData)
        header = header.rstrip('\n')
        column_names = header.split(",")
        columns_mapping = {}

        for i, column_name in enumerate(column_names):
            columns_mapping[column_name] = i
        reader = csv.reader(corporateData)
        count_per_year = [0] * 100

        for row in reader:
            registration_date = row[columns_mapping['DATE_OF_REGISTRATION']]
            last_two_digits = registration_date[-2:]
            if last_two_digits == "NA":
                continue
            count_per_year[int(last_two_digits)] += 1
    return count_per_year


def plot_registration_data(count_data):
    plt.bar(list(range(0, 100)), count_data)
    plt.show()


if __name__ == "__main__":
    registration_count = process_csv_data()
    plot_registration_data(registration_count)