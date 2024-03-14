# 1. Histogram of Authorized Cap

import matplotlib.pyplot as plt
import csv


def load_data(filename='Maharashtra.csv'):
    file_obj = open(filename, encoding='unicode_escape')
    corporateData = csv.reader(file_obj)
    header = next(file_obj).split(',')
    return file_obj, corporateData, header


def initialize_bins():
    lower_limits = [0, 1e5+1, 1e6+1, 1e7+1, 1e8+1]
    upper_limits = [1e5, 1e6, 1e7, 1e8, 1e18]
    return lower_limits, upper_limits


def initialize_labels():
    categories = ['<= 1L', '1L to 10L', '10L to 1Cr', '1Cr to 10Cr', '> 10Cr']
    return categories


def initialize_columns(header):
    columns_mapping = {}
    for i, col in enumerate(header):
        columns_mapping[col] = i
    return columns_mapping


def process_data(file_obj, corporateData, columns):
    count_per_category = [0] * 5

    for data in corporateData:
        authorized_cap = float(data[columns['AUTHORIZED_CAP']])
        for i in range(5):
            if lower_limits[i] <= authorized_cap <= upper_limits[i]:
                count_per_category[i] += 1
    file_obj.close()
    return count_per_category


def plot_data(categories, counts):
    plt.bar(categories, counts)
    plt.show()


if __name__ == "__main__":
    file_obj, reader_obj, heading = load_data()
    lower_limits, upper_limits = initialize_bins()
    categories = initialize_labels()
    columns_mapping = initialize_columns(heading)
    count_per_category = process_data(file_obj, reader_obj, columns_mapping)
    plot_data(categories, count_per_category)