WITH base AS (
    SELECT
        visited_on,
        SUM(amount) AS amount
    FROM Customer
    GROUP BY visited_on
)
SELECT
    visited_on,
    7_days_amount AS amount,
    ROUND(7_days_amount / 7, 2) AS average_amount
FROM (
    SELECT
        visited_on,
        DATE_SUB(visited_on, INTERVAL 6 DAY) AS 6_days_before,
        SUM(amount) OVER (ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS 7_days_amount
    FROM base
) AS v
WHERE 6_days_before IN (SELECT DISTINCT visited_on FROM Customer)
ORDER BY visited_on;