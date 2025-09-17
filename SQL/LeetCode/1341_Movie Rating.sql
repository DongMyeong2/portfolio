WITH base AS (
    SELECT
        r.movie_id,
        m.title,
        r.user_id,
        u.name,
        r.rating,
        r.created_at
    FROM MovieRating  AS r
        INNER JOIN Movies AS m USING(movie_id)
        INNER JOIN Users AS u USING(user_id)
)
SELECT results
FROM (
    SELECT name AS results
    FROM base
    GROUP BY user_id
    ORDER BY COUNT(user_id) DESC, name
    LIMIT 1
) AS n
UNION ALL
SELECT results
FROM (
    SELECT title AS results
    FROM base
    WHERE YEAR(created_at) = '2020' AND MONTH(created_at) = '2'
    GROUP BY movie_id
    ORDER BY AVG(rating) DESC, title
    LIMIT 1
) AS m;