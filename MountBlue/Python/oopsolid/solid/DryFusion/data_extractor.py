class DataExtractor:

    def __init__(self):
        self.filename = ""
        self.data = []
        self.col_name_vs_index = {}
        self.col_name_vs_data = {}
        self.index_vs_col_name = {}

    def set_path(self, filename):
        self.filename = filename

    def __get_column_from_index(self, index):
        if index not in self.index_vs_col_name:
            return -1
        return self.index_vs_col_name[index]

    def __create_index_vs_col_name_dict(self):
        for key, index_range in self.col_name_vs_index.items():
            start_index = index_range[0]
            end_index = index_range[1]
            for index in range(start_index, end_index+1):
                self.index_vs_col_name[index] = key

    def __find_leaked_data(self, string, data_index):
        # ex
        start_index = data_index[0]
        end_index = data_index[1]

        left_leak = ''
        right_leak = ''

        # find current column name
        current_col_name = self.__get_column_from_index(start_index)

        # find the left leaked data
        for i in range(start_index-1, -1, -1):

            # while seaching the left leaked data if it is going to some other columns area return 'NA'
            if (self.__get_column_from_index(i) != -1 and
                    self.__get_column_from_index(i) != current_col_name):
                if string[i] != ' ':
                    return 'NA', 'NA'

            char = string[i]
            if char == ' ' or char == '\n':
                break
            left_leak = char + left_leak

        # find the right leaked data
        for j in range(end_index+1, len(string)):

            char = string[j]

            # while seaching the right leaked data if it is going to some other columns area return 'NA'
            if (self.__get_column_from_index(j) != -1 and
                    self.__get_column_from_index(j) != current_col_name):

                if char != ' ':
                    return 'NA', 'NA'

            if char == ' ' or char == '\n':
                break
            right_leak += char
        return left_leak, right_leak

    def __get_data_from_line(self, line, index):
        start_index = index[0]
        end_index = index[1]
        col_data = ''
        data_index = []

        try:
            for i in range(start_index, end_index+1):
                if line[i] != '\n' and line[i] != ' ':
                    col_data += line[i]
                    data_index.append(i)
        except IndexError:
            return 'NA'

        # if the data is not present
        if not self.__data_is_valid(col_data):
            data_index.append(start_index)
            data_index.append(end_index)
            col_data = 'NA'

        # from the data index find the start and end index of the actual data
        left_data, right_data = self.__find_leaked_data(
            line, [data_index[0], data_index[-1]])

        # if leftdata or rightdata is NA that means they are going others columns
        if (left_data == 'NA' or right_data == 'NA'):
            return 'NA'

        # if col_data is empty and left_data or right data is empty
        if (col_data == 'NA' and (left_data != '' or right_data != '')):
            return left_data + right_data
        col_data = left_data + col_data + right_data
        return col_data

    def __data_is_valid(self, col_data):
        """col_data empty or not"""
        if len(col_data.strip()) == 0:
            return False
        return True

    def extract_data(self):
        with open(self.filename, 'r', encoding='utf8') as file:
            for line in file:
                self.data.append(line)
        self.__extract_header(self.data)
        self.__create_index_vs_col_name_dict()

        # initialize the dictionary
        for column in enumerate(self.col_name_vs_index):
            self.col_name_vs_data[column[1]] = []

        # iterate throught the each row (one one line)
        for line in self.data[1:]:
            # if the line data is invalid then do not extract that line
            if not self.__data_is_valid(line):
                continue
            for column, index in self.col_name_vs_index.items():

                # find the data between the start index and end index
                # index ---> is a tuple here
                col_data = self.__get_data_from_line(line, index)

                # get the list for that column and add the column data
                self.col_name_vs_data[column].append(col_data.strip())

    def __extract_header(self, data):
        first_line = data[0]
        col_name = ''
        start_index = 0
        flag = False

        for i, char in enumerate(first_line):
            char = first_line[i]
            if char != ' ':
                if not flag:
                    flag = True
                    start_index = i
                if char == '\n':
                    self.col_name_vs_index[col_name] = (start_index, i-1)
                    return
                col_name += char

            else:
                if flag:
                    self.col_name_vs_index[col_name] = (start_index, i-1)
                    flag = False
                    col_name = ''

    def show_data(self):
        for column, values in self.col_name_vs_data.items():
            print(column, values)

    def get_data(self):
        self.col_name_vs_data.clear()
        self.col_name_vs_index.clear()
        self.data.clear()
        self.extract_data()
        return self.col_name_vs_data
