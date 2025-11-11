WITH base AS (
  SELECT
    DISTINCT
      user_id,
      FIRST_VALUE(post_date) OVER (PARTITION BY user_id ORDER BY post_date ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS first_date,
      LAST_VALUE(post_date) OVER (PARTITION BY user_id ORDER BY post_date ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS last_date
  FROM posts
  WHERE user_id IN (
    SELECT
      DISTINCT user_id
    FROM posts
    WHERE YEAR(post_date) = 2021
    GROUP BY user_id
    HAVING COUNT(user_id) > 1
  )
)

SELECT
  user_id,
  DATEDIFF(last_date, first_date) AS days_between
FROM base;