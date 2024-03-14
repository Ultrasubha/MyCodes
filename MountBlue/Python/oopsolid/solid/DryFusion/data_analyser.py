import sys


class DataAnalyzer:
    def __init__(self) -> None:
        self.data = {}

    def set_data(self, data):
        self.data = data

    def find_min_diff(self, column1, column2, query_column_name):
        column1_data = self.data[column1]
        column2_data = self.data[column2]

        min_index = -1
        min_value = sys.maxsize
        for index, value in enumerate(column1_data):
            try:
                value1 = float(value)
                value2 = float(column2_data[index])
            except ValueError:
                continue
            diff = abs(value1 - value2)
            if diff < min_value:
                min_value = diff
                min_index = index
        print(self.data[query_column_name][min_index])
