-- Number of matches won per team per year in IPL.

SELECT season, winner, COUNT(winner) AS matches_won
FROM ipl_matches
WHERE winner IS NOT NULL
GROUP BY season, winner
ORDER BY season, winner;
