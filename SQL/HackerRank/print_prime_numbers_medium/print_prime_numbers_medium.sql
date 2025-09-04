WITH RECURSIVE nums(x) AS (
    SELECT 2 AS x
    UNION ALL
    SELECT x+1 FROM nums WHERE x < 1000
), divs(y) AS (
    SELECT 2 AS y
    UNION ALL
    SELECT y+1 FROM divs WHERE y < 1000
)
SELECT group_concat(x ORDER BY x separator '&') AS primes
FROM nums
WHERE NOT EXISTS (SELECT y FROM divs WHERE y * y <= x AND MOD(x, y) = 0);
