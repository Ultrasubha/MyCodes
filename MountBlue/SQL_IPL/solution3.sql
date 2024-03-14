-- Number of umpires in IPL by country except India
-- SELECT DISTINCT country, count(country) FROM ipl_umpires 
-- WHERE country NOT LIKE '%India%' GROUP BY country;
SELECT country, count(*) as "umpires"
FROM (
    SELECT umpire1 AS umpire FROM ipl_matches WHERE umpire1 !=''
    UNION
    SELECT umpire2 AS umpire FROM ipl_matches WHERE umpire2 !=''
) AS sq JOIN ipl_umpires
ON sq.umpire = ipl_umpires.umpire 
GROUP BY country 
HAVING country NOT LIKE '%India%'