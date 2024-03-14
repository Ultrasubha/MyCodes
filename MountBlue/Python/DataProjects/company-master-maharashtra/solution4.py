# 4. Grouped Bar Plot
import csv
import matplotlib.pyplot as plt


def process_registration_data():
    data_by_month = {}
    business_labels = {}
    with open('Maharashtra.csv', encoding='unicode_escape') as file:
        heading = next(file)
        heading = heading.rstrip('\n')
        column_names = heading.split(",")
        columns_mapping = {}
        for i, column_name in enumerate(column_names):
            columns_mapping[column_name] = i
        maharashtraData = csv.reader(file)
        for company in maharashtraData:
            registration_month = company[columns_mapping['DATE_OF_REGISTRATION']][-2:]
            if registration_month == "NA":
                continue
            registration_month = int(registration_month)
            if registration_month <= 11 or registration_month > 21:
                continue
            if registration_month not in data_by_month:
                data_by_month[registration_month] = {}
            business_activity = company[columns_mapping['PRINCIPAL_BUSINESS_ACTIVITY_AS_PER_CIN']]
            business_labels[business_activity] = business_labels.get(business_activity, 0) + 1
            data_by_month[registration_month][business_activity] = data_by_month[registration_month].get(business_activity, 0) + 1
    return data_by_month, business_labels


def plot_data_by_month(data_by_month, top_business_labels):
    arr2d = []
    for label in top_business_labels:
        tmp = [data_by_month[month].get(label, 0) for month in data_by_month]
        arr2d.append(tmp)
    bar_width = 0.2
    positions = list(data_by_month.keys())
    plt.figure(figsize=(12, 10))
    for i, label in enumerate(top_business_labels):
        plt.bar([pos + bar_width * (i - len(top_business_labels) / 2) for pos in positions], arr2d[i], bar_width)
    plt.legend(top_business_labels)
    plt.show()


if __name__ == "__main__":
    data_by_month, business_labels = process_registration_data()
    top_business_labels = list(dict(sorted(business_labels.items(), key=lambda x: x[1], reverse=True)).keys())[:5]
    plot_data_by_month(data_by_month, top_business_labels)
