SELECT season, SUM(season) AS Total_Matches 
FROM ipl_matches 
GROUP BY season 
ORDER BY season;