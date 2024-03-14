import unittest
from solution import Solution


class TestSol(unittest.TestCase):

    def setUp(self):
        self.solution = Solution('mock_matches.csv', 'mock_deliveries.csv')

    def test_no_of_matches_per_year(self):
        value = {2015 : 3, 2016 : 4}
        self.assertEqual(self.solution.no_of_matches_per_year(), value)

    def test_matches_won_for_all_team_all_year(self):
        value = {'KKR': {2015: 1, 2016: 1}, 'CSK': {2015: 1, 2016: 1}, 'MI': {2015: 1, 2016: 2}}
        self.assertEqual(self.solution.matches_won_for_all_team_all_year(), value)

    def test_runs_concluded_per_team_2016(self):
        value = {'KKR': 2, 'MI': 2, 'CSK': 4}
        self.assertEqual(self.solution.runs_concluded_per_team_2016(), value)


if __name__ == '__main__':
    unittest.main()
