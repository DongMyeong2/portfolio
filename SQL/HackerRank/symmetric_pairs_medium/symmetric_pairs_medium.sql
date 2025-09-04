WITH same AS (
    SELECT X, Y
    FROM Functions
    WHERE X = Y
    GROUP BY X, Y
    HAVING COUNT(*) > 1
), diff AS (
    SELECT X, Y
    FROM Functions
    WHERE X <> Y
)
SELECT *
FROM (
    SELECT X, Y
    FROM same
    UNION ALL
    SELECT
        d1.X, d1.Y
    FROM diff AS d1 INNER JOIN diff AS d2 ON d1.X=d2.Y AND d1.Y=d2.X
    WHERE d1.X < d1.Y
    ) AS final
ORDER BY X, Y;
