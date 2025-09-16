WITH category_name AS (
    SELECT
        'Low Salary' AS category
    UNION ALL
    SELECT
        'Average Salary' AS category
    UNION ALL
    SELECT
        'High Salary' AS category
), set_category AS (
    SELECT
        category,
        COUNT(category) AS `accounts_count`
    FROM (
        SELECT
            *,
            CASE
                WHEN income < 20000 THEN 'Low Salary'
                WHEN income BETWEEN 20000 AND 50000 THEN 'Average Salary'
                WHEN income > 50000 THEN 'High Salary'
            END AS category
        FROM Accounts
    ) AS base
    GROUP BY category
)
SELECT
    n.category,
    COALESCE(accounts_count, 0) AS accounts_count
FROM category_name AS n LEFT JOIN set_category AS c USING(category);