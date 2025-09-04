WITH RECURSIVE nums(n) AS (
  SELECT 20
  UNION ALL
  SELECT n - 1 FROM nums WHERE n > 1
)
SELECT RTRIM(REPEAT('* ', n)) AS pattern
FROM nums;
