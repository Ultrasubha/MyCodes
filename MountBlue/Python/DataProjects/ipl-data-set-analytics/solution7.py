# Q.7) Extra runs conceded per team in the year 2016.

import csv
import matplotlib.pyplot as plt


def calculate(year):
    match_ids = []
    with open('matches.csv', 'r') as matches:
        for match in csv.DictReader(matches):
            if match['season'] == year:
                match_ids.append(int(match["id"]))

    with open('deliveries.csv', 'r') as deliveries:
        extra_runs_by_team = {}
        for delivery in csv.DictReader(deliveries):
            team = delivery["bowling_team"]
            extra_run = int(delivery["extra_runs"])

            if int(delivery["match_id"]) in match_ids:
                if team not in extra_runs_by_team:
                    extra_runs_by_team[team] = 0
                extra_runs_by_team[team] += extra_run

    return extra_runs_by_team


def plot(extra_runs_by_team):
    team = list(extra_runs_by_team.keys())
    extra_runs = list(extra_runs_by_team.values())

    plt.figure(figsize=(10, 6))
    plt.bar_label(plt.bar(team, extra_runs), padding=5)
    plt.bar(team, extra_runs, color='#ff0000', width=0.8)
    plt.title('Extra Runs Conceded per Team in IPL 2016')
    plt.xlabel('Team')
    plt.ylabel('Extra Runs Conceded')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()


def execute():
    extra_runs_by_team = calculate("2016")
    print(extra_runs_by_team)
    plot(extra_runs_by_team)


execute()
