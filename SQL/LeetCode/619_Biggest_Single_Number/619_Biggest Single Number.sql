SELECT
    IF(cnt > 1, null , num) AS num
FROM (
    SELECT
        num,
        COUNT(*) AS cnt
    FROM MyNumbers
    GROUP BY num
    ORDER BY COUNT(*), num DESC
    LIMIT 1
) AS base;