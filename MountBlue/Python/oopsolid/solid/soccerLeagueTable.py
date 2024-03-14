# Part Two: Soccer League Table

def find_team_with_smallest_difference(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    # Removing header and footer
    data_lines = lines[1:-1]
    min_difference_team = None
    min_difference = float('inf')
    for line in data_lines:
        columns = line.split()
        if len(columns) >= 10:
            team = columns[1]
            goals_for = int(columns[6])
            goals_against = int(columns[8])
            difference = abs(goals_for - goals_against)

            if difference < min_difference:
                min_difference = difference
                min_difference_team = team
    return min_difference_team


result = find_team_with_smallest_difference('/home/urahara/Documents/oopsolid/data/football.dat')
print(f"The team with the smallest difference between 'for' and 'against' goals is: {result}")
