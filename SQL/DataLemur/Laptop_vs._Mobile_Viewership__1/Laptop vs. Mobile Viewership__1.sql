# case 1
WITH base AS (
  SELECT
    device_type,
    COUNT(device_type) AS cnt
  FROM (
    SELECT
      IF(device_type IN ('tablet', 'phone'), 'mobile', device_type) AS device_type
    FROM viewership
  ) AS a
  GROUP BY device_type
)

SELECT
  MAX(laptop_views) AS 'laptop_views',
  MAX(mobile_views) AS 'mobile_views'
FROM (
  SELECT
    IF(device_type = 'laptop', cnt, null) AS 'laptop_views',
    IF(device_type = 'mobile', cnt, null) AS 'mobile_views'
  FROM base
) AS b;

# case 2
SELECT
  SUM(CASE WHEN device_type = 'laptop' THEN 1 ELSE 0 END) AS laptop_views,
  SUM(CASE WHEN device_type IN ('tablet', 'phone') THEN 1 ELSE 0 END) AS mobile_views
FROM viewership;