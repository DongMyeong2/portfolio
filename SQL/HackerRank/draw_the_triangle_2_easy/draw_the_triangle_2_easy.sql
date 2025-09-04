WITH RECURSIVE nums(n) AS (
  SELECT 1
  UNION ALL
  SELECT n + 1 FROM nums WHERE n < 20
)
SELECT RTRIM(REPEAT('* ', n)) AS pattern
FROM nums;
