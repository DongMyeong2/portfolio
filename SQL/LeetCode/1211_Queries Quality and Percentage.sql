SELECT 
    query_name,
    ROUND(AVG(ratio), 2) AS quality,
    ROUND(AVG(rating) * 100, 2) AS poor_query_percentage
FROM (
    SELECT
        query_name,
        rating / position AS `ratio`,
        IF(rating < 3, 1, 0) AS rating
    FROM Queries
) AS base
GROUP BY query_name