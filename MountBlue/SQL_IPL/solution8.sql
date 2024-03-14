-- Top 10 economical bowlers in the year 2015

WITH BowlerRuns AS (
    SELECT
        d.bowler,
        COUNT(*) AS balls,
        SUM(d.total_runs) AS total_runs
    FROM ipl_deliveries d
    JOIN ipl_matches m ON d.match_id = m.id
    WHERE m.season = '2015'
    GROUP BY d.bowler
)

SELECT
    br.bowler,
    (SUM(br.total_runs) / SUM(br.balls)) * 6 AS economy
FROM BowlerRuns br
GROUP BY br.bowler
ORDER BY economy
LIMIT 10;