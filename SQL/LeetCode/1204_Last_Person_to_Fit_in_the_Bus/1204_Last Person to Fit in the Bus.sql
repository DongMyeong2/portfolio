SELECT
    person_name
FROM (
    SELECT
        person_name,
        SUM(weight) OVER (ORDER BY turn ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS total_weight
    FROM Queue
) AS base
WHERE total_weight <= 1000
ORDER BY total_weight DESC
LIMIT 1;