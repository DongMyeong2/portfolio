SELECT
    DISTINCT
        num AS ConsecutiveNums
FROM (
    SELECT
        id,
        num,
        IF(num = LEAD(num) OVER () AND num = LEAD(num, 2) OVER (), 'Y', 'N') AS check_consecutive
    FROM Logs
) AS base
WHERE check_consecutive = 'Y';