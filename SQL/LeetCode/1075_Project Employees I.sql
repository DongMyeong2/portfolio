WITH base AS (
    SELECT
        p.project_id,
        p.employee_id,
        e.experience_years
    FROM Project AS p LEFT JOIN Employee AS e USING(employee_id)
)
SELECT
    project_id,
    ROUND(SUM(experience_years) / COUNT(experience_years), 2) AS average_years
FROM base
GROUP BY project_id