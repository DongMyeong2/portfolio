WITH base AS (
  SELECT
    e1.employee_id AS employee_id,
    e1.name,
    e1.salary AS employee_salary,
    e2.employee_id AS manager_id,
    e2.salary AS manager_salary
  FROM employee AS e1 LEFT JOIN employee AS e2 ON e1.manager_id = e2.employee_id
)
SELECT
  employee_id,
  name AS employee_name
FROM base
WHERE employee_salary > manager_salary;