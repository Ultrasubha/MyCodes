-- Extra runs conceded per team in the year 2016
SELECT
    deliveries.bowling_team AS team,
    SUM(deliveries.extra_runs) AS extra_runs_conceded
FROM ipl_deliveries AS deliveries
JOIN ipl_matches AS matches ON deliveries.match_id = matches.id
WHERE matches.season = 2016
GROUP BY deliveries.bowling_team
ORDER BY extra_runs_conceded DESC;
