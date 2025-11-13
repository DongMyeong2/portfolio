WITH base AS (
  SELECT
    user_id,
    COUNT(user_id) AS user_orders
  FROM trades
  WHERE status = 'Completed'
  GROUP BY user_id
)

SELECT
  city,
  SUM(user_orders) AS total_orders
FROM users AS u INNER JOIN base AS b ON u.user_id = b.user_id
GROUP BY city
ORDER BY total_orders DESC
LIMIT 3;