# Part One: Weather Data

def find_day_with_smallest_spread(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    # Removing header and footer
    data_lines = lines[2:-1]
    min_spread_day = None
    min_spread = float('inf')

    for line in data_lines:
        columns = line.split()
        day = int(columns[0])
        # Handle cases where there is an asterisk (*) in the temperature columns
        try:
            max_temp = int(columns[1])
            min_temp = int(columns[2].rstrip('*'))
        except ValueError:
            continue
        spread = max_temp - min_temp
        if spread < min_spread:
            min_spread = spread
            min_spread_day = day
    return min_spread_day


result = find_day_with_smallest_spread('/home/urahara/Documents/oopsolid/data/weather.dat')
print(f"The day number with the smallest temperature spread is: {result}")
