WITH base AS (
  SELECT
    DISTINCT
      user_id,
      COUNT(user_id) OVER (PARTITION BY user_id) AS tweet_bucket
  FROM tweets
  WHERE YEAR(tweet_date) = '2022'
)

SELECT
  tweet_bucket,
  COUNT(*) AS users_num
FROM base
GROUP BY tweet_bucket
ORDER BY tweet_bucket;