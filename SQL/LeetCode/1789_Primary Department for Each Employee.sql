SELECT 
    employee_id,
    department_id
FROM (
    SELECT 
        *,
        CASE
            WHEN COUNT(employee_id) OVER (PARTITION BY employee_id) > 1 AND  primary_flag = 'Y' THEN 'Y'
            WHEN COUNT(employee_id) OVER (PARTITION BY employee_id) = 1 THEN 'Y'
            ELSE 'N'
        END AS `primary_check`
    FROM Employee
) AS base
WHERE primary_check = 'Y';