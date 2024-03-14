# Top batsman for Royal Challengers Bangalore

import csv
import matplotlib.pyplot as plt


def calculate():
    total_runs_by_batsman = {}
    with open('deliveries.csv', 'r') as deliveries:
        for delivery in csv.DictReader(deliveries):
            batsman = delivery['batsman']
            batting_team = delivery['batting_team']
            total_runs = int(delivery['total_runs'])

            if batting_team == 'Royal Challengers Bangalore':
                total_runs_by_batsman[batsman] = total_runs_by_batsman.get(
                                                    batsman, 0) + total_runs

    batsman_runs_list = [(batsman, runs) for batsman, runs in
                         total_runs_by_batsman.items()]
    batsman_runs_list.sort(key=lambda x: x[1], reverse=True)
    top_10_batsmen, runs = zip(*batsman_runs_list[:10])

    return top_10_batsmen, runs


def plot(top_10_batsmen, runs):
    # Plotting the bar chart
    plt.figure(figsize=(12, 6))
    plt.bar(top_10_batsmen, runs, color='skyblue')
    plt.title('Total Runs Scored by Top 10 Batsmen for RCB')
    plt.xlabel('Batsman')
    plt.ylabel('Total Runs')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()


def execute():
    top_10_batsmen, runs = calculate()
    plot(top_10_batsmen, runs)


execute()
