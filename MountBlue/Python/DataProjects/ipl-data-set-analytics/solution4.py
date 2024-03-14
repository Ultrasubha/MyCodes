import csv
import matplotlib.pyplot as plt


def calculate():
    games_by_teams_by_season = {}
    with open('matches.csv', 'r', encoding="utf8") as csvfile:
        matches = csv.DictReader(csvfile)
        teams_set = set()

        for match in matches:
            season = match['season']
            team1 = match['team1']
            team2 = match['team2']
            teams_set.add(team1)
            teams_set.add(team2)

            if season not in games_by_teams_by_season:
                games_by_teams_by_season[season] = {}
            if team1 not in games_by_teams_by_season[season]:
                games_by_teams_by_season[season][team1] = 0
            if team2 not in games_by_teams_by_season[season]:
                games_by_teams_by_season[season][team2] = 0

            games_by_teams_by_season[season][team1] += 1
            games_by_teams_by_season[season][team2] += 1

    return games_by_teams_by_season, list(sorted(teams_set))


def plot(games_by_teams_by_season, teams_list):
    seasons = list(sorted(games_by_teams_by_season.keys()))
    plt.figure(figsize=(12, 6))
    bottom = [0] * len(seasons)

    for team in teams_list:
        values = []
        for season in seasons:
            data = 0
            if team in games_by_teams_by_season[season]:
                data = games_by_teams_by_season[season][team]
            values.append(data)
        plt.bar(seasons, values, bottom=bottom)
        for i, value in enumerate(values):
            bottom[i] += value
        values.clear()

    plt.xlabel("seasons")
    plt.ylabel("Matches Player per Team")
    plt.title("Mathes Played by team by seasons")
    plt.legend(teams_list, bbox_to_anchor=(1, 1), loc='upper left')
    plt.tight_layout()
    plt.show()


def execute():
    games_by_teams_by_season, teams_set = calculate()
    plot(games_by_teams_by_season, teams_set)


execute()
