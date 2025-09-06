WITH base AS (
    SELECT
        *,
        LAG(recordDate) OVER (ORDER BY recordDate) AS pre_recordDate,
        LAG(temperature) OVER (ORDER BY recordDate) AS pre_temperature
    FROM Weather
)

SELECT id
FROM (
    SELECT
        id,
        IF(temperature > pre_temperature, 1, null) AS `check_temp`
    FROM base
    WHERE DATEDIFF(recordDate, pre_recordDate) = 1
) AS w
WHERE check_temp = 1