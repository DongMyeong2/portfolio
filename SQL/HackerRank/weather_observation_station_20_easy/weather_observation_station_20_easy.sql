WITH ordered AS (
    SELECT
        LAT_N,
        ROW_NUMBER() OVER (ORDER BY LAT_N) AS rn,
        COUNT(*) OVER () AS total
    FROM STATION
)
SELECT ROUND(AVG(LAT_N), 4)
FROM ordered
WHERE rn IN (FLOOR((total + 1) / 2), CEIL((total + 1) / 2));
