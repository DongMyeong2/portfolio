WITH base AS (
    SELECT
        d.name AS Department,
        e.name AS Employee,
        e.salary AS Salary
    FROM Employee AS e INNER JOIN Department AS d ON e.departmentId = d.id
)

SELECT
    Department,
    Employee,
    Salary
FROM (
    SELECT
        *,
        DENSE_RANK() OVER (PARTITION BY Department ORDER BY Salary DESC) AS d_rank
    FROM base
) AS b
WHERE d_rank <= 3;