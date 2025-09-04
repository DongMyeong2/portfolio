WITH base AS (
    SELECT
        *,
        IF (LEAD(Start_Date) OVER (ORDER BY End_Date) = End_Date, null, 1) AS `check`
    FROM Projects
), set_group AS(
    SELECT
        MIN(Start_Date) OVER (PARTITION BY `group`) AS `Start_Date,
        MAX(End_Date) OVER (PARTITION BY `group`) AS `End_Date`
    FROM (
        SELECT
            Start_Date,
            End_Date,
            COUNT(`check`) OVER (ORDER BY End_Date ROWS BETWEEN UNBOUNDED PRECEDING AND 1 PRECEDING) AS `group`
        FROM base
        ) AS check_cnt
)
SELECT 
    Start_Date,
    End_Date
FROM (
    SELECT
        Start_Date,
        End_Date,
        COUNT(*) AS cnt
    FROM set_group
    GROUP BY Start_Date, End_Date
    ) AS final
ORDER BY cnt, Start_Date;
