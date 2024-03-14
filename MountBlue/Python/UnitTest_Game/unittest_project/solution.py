import csv


class Solution:
    def __init__(self, matchesfile, deliveriesfile) -> None:
        self.matches = matchesfile
        self.deliveries = deliveriesfile

    def no_of_matches_per_year(self):
        with open(self.matches, 'r') as csvfile:
            matches_reader = csv.DictReader(csvfile)
            year_vs_match = {}
            for match in matches_reader:
                year = int(match['season'])
                if year not in year_vs_match:
                    year_vs_match[year] = 0
                year_vs_match[year] += 1
        return year_vs_match       

    def matches_won_for_all_team_all_year(self):
        with open('mock_matches.csv', 'r') as csvfile:
            matches_reader = csv.DictReader(csvfile)
            teams = set()
            win_year_team = {}
            for match in matches_reader:
                teams.add(match['team1'])
                teams.add(match['team2'])
                year = int(match['season'])
                winner = match['winner']

                if winner not in win_year_team:
                    win_year_team[winner] = {}
                if year not in win_year_team[winner]:
                    win_year_team[winner][year] = 0
                win_year_team[winner][year] += 1        

        return win_year_team

    def runs_concluded_per_team_2016(self):
        YEAR = 2016
        match_ids = []
        with open(self.matches, 'r') as csvfile:
            matches_reader = csv.DictReader(csvfile)

            for matches in matches_reader:
                if int(matches['season']) == YEAR:
                    match_ids.append(matches['id'])
        with open(self.deliveries) as csvfile:
            deliveries_reader = csv.DictReader(csvfile)
            team_vs_extraruns = {}
            for delivery in deliveries_reader:
                match_id = delivery['match_id']
                if match_id in match_ids:
                    bowling_team = delivery['bowling_team']
                    extra_runs = int(delivery['extra_runs'])

                    if bowling_team not in team_vs_extraruns:
                        team_vs_extraruns[bowling_team] = 0
                    team_vs_extraruns[bowling_team] += extra_runs
        return team_vs_extraruns


solution = Solution('mock_matches.csv', 'mock_deliveries.csv')
print(solution.no_of_matches_per_year())
