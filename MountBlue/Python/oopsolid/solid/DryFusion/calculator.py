from data_extractor import DataExtractor
from data_analyser import DataAnalyzer


class Calculator:
    def __init__(self, extractor, analyzer) -> None:
        self.extractor = extractor
        self.analyzer = analyzer

    def execute(self, column1, column2, query_column_name):
        data = self.extractor.get_data()
        self.analyzer.set_data(data)
        self.analyzer.find_min_diff(column1, column2, query_column_name)


def main():
    extractor = DataExtractor()
    analyzer = DataAnalyzer()

    extractor.set_path('/home/urahara/Documents/oopsolid/data/football.dat')
    calculator = Calculator(extractor, analyzer)
    calculator.execute('F', 'A', 'Team')

    extractor.set_path('/home/urahara/Documents/oopsolid/data/weather.dat')
    calculator = Calculator(extractor, analyzer)
    calculator.execute('MxT', 'MnT', 'Dy')


if __name__ == '__main__':
    main()
