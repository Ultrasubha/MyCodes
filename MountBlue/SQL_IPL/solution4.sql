SELECT
    season,
    team,
    COUNT(team) AS games_played
FROM (
    SELECT season, team1 AS team FROM ipl_matches
    UNION ALL
    SELECT season, team2 AS team FROM ipl_matches
) AS teams_played
GROUP BY season, team
ORDER BY season, team;
