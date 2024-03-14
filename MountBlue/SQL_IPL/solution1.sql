-- 1.Total runs scored by team
SELECT batting_team, SUM(total_runs) 
FROM ipl_deliveries 
GROUP BY batting_team;