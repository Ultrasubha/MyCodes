import csv
import matplotlib.pyplot as plt


def calculate():
    match_ids_of_2015 = []

    with open('matches.csv', 'r') as csvfile:
        matches = csv.DictReader(csvfile)
        for match in matches:
            season = match['season']
            match_id = int(match['id'])

            if season == '2015':
                match_ids_of_2015.append(match_id)

    bowler_to_run_dict = {}

    with open('deliveries.csv', 'r') as csvfile:
        deliveries_reader = csv.DictReader(csvfile)
        for deliveries in deliveries_reader:
            match_id = int(deliveries['match_id'])
            if match_id in match_ids_of_2015:
                bowler = deliveries['bowler']
                runs = int(deliveries['total_runs'])
                if bowler not in bowler_to_run_dict:
                    bowler_to_run_dict[bowler] = [0, 0]
                bowler_to_run_dict[bowler][0] += 1
                bowler_to_run_dict[bowler][1] += runs

    for bowler, temp_list in bowler_to_run_dict.items():
        economy = (temp_list[1] / temp_list[0]) * 6
        temp_list.clear()
        temp_list.append(economy)
    sorted_bowler_economy = dict(
        sorted(bowler_to_run_dict.items(), key=lambda x: x[1][0])[:10])

    return sorted_bowler_economy


def plot(bowler_to_run_dict):
    bowlers = list(bowler_to_run_dict.keys())
    economies = []
    for economy in bowler_to_run_dict.values():
        economies.append(float(format(economy[0], ".2f")))
    plt.figure(figsize=(12, 8))
    plt.bar(bowlers, economies)
    plt.xlabel('Economy rate')
    plt.title('Top 10 economical bowlers in IPL 2015')
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()


def execute():
    bowler_to_run_dict = calculate()
    print(bowler_to_run_dict)
    plot(bowler_to_run_dict)


execute()
