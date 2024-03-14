# Q.1) Total runs scored by team

import csv
import matplotlib.pyplot as plt


def calculate():
    total_runs_by_team = {}
    with open('deliveries.csv', 'r') as deliveries:
        for delivery in csv.DictReader(deliveries):
            batting_team = delivery['batting_team']
            total_runs = int(delivery['total_runs'])
            total_runs_by_team[batting_team] = total_runs_by_team.get(
                                                batting_team, 0) + total_runs

    team_runs_list = [(team, runs)
                      for team, runs in total_runs_by_team.items()]
    team_runs_list.sort(key=lambda x: x[1], reverse=True)
    teams, runs = zip(*team_runs_list)

    return teams, runs


def plot(teams, runs):
    # Plotting the bar chart
    plt.figure(figsize=(12, 6))
    plt.bar(teams, runs, color='skyblue')
    plt.title('Total Runs Scored by Each IPL Team')
    plt.xlabel('Team')
    plt.ylabel('Total Runs')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()


def execute():
    teams, runs = calculate()
    plot(teams, runs)


execute()
