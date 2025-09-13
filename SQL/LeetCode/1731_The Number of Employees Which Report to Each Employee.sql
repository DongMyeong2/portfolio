SELECT
    e.employee_id,
    e.name,
    r.reports_count,
    r.average_age
FROM Employees AS e
    INNER JOIN (
        SELECT
            reports_to,
            COUNT(reports_to) AS reports_count,
            ROUND(AVG(age)) AS average_age
        FROM Employees
        GROUP BY reports_to
    ) AS r ON e.employee_id = r.reports_to
ORDER BY e.employee_id;