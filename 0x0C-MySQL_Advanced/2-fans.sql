-- SQL script that ranks country origins of bands
-- following these requirements
SELECT origin AS origin, SUM(fans) as nb_fans
From metal_bands GROUP BY origin ORDER BY nb_fans DESC;