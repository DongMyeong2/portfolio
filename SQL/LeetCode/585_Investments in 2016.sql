WITH base AS (
    SELECT
        *,
        COUNT(*) OVER (PARTITION BY lat, lon) AS check_1,
        COUNT(*) OVER (PARTITION BY tiv_2015) AS check_2
    FROM Insurance
)

SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM base
WHERE check_1 = 1 AND check_2 > 1;