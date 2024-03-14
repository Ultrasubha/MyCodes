-- top 10 batsmen by runs scored in RCB
SELECT batsman, SUM(batsman_runs) AS runs 
FROM ipl_deliveries 
WHERE batting_team = 'Royal Challengers Bangalore' 
GROUP BY batsman 
ORDER BY runs desc
LIMIT 10; 