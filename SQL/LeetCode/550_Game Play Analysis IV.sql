WITH base AS (
    SELECT
        *
    FROM (
        SELECT
            player_id,
            event_date,
            FIRST_VALUE(event_date) OVER (PARTITION BY player_id ORDER BY event_date) AS first_logged_date,
            IF(DATEDIFF(LEAD(event_date) OVER (PARTITION BY player_id ORDER BY event_date), event_date) = 1, 1, 0) AS check_day_after_day
        FROM Activity
    ) AS a
    WHERE event_date = first_logged_date
)
SELECT
    ROUND(AVG(check_day_after_day), 2) AS fraction 
FROM base;