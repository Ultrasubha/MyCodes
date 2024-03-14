# 3. Company registration in the year 2015 by the district

import csv
import matplotlib.pyplot as plt


def process_pincode_data():
    pincode_obj = {}
    with open('Maharashtra.csv', encoding='unicode_escape') as file:
        heading = next(file)
        heading = heading.rstrip('\n')
        column_names = heading.split(",")
        columns_mapping = {}
        for i, column_name in enumerate(column_names):
            columns_mapping[column_name] = i

        reader = csv.reader(file)
        for row in reader:
            address = row[columns_mapping['Registered_Office_Address']]
            address_tokens = address.split(" ")
            pincode = address_tokens[-1]

            if pincode == '' or row[columns_mapping['DATE_OF_REGISTRATION']][-2:] != '15':
                continue
            pincode_obj[pincode] = pincode_obj.get(pincode, 0) + 1
    return pincode_obj


def read_pincode_district_mapping():
    district_mapping = {}
    with open('pincode.csv', encoding='unicode_escape') as file:
        column_names = next(file).rstrip('\n').split(",")
        columns_mapping = {}
        for i, column_name in enumerate(column_names):
            columns_mapping[column_name] = i
        reader = csv.reader(file)
        for row in reader:
            district_mapping[row[columns_mapping['Pin Code']]] = row[columns_mapping['District']]
    return district_mapping


def plot_pincode_data(pincode_data, district_mapping):
    districts = []
    counts = []
    for pincode, count in pincode_data.items():
        if pincode in district_mapping:
            districts.append(district_mapping[pincode])
            counts.append(count)

    plt.figure(figsize=(12, 6))
    plt.bar(districts, counts)
    plt.xticks(rotation=45, ha='right')
    plt.show()


if __name__ == "__main__":
    pincode_data = process_pincode_data()
    district_mapping = read_pincode_district_mapping()
    plot_pincode_data(pincode_data, district_mapping)