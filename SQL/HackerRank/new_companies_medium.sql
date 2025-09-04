-- WITH문 사용 (MySQL 8.0 이상)
WITH cte AS (
    SELECT 
        company_code,
        COUNT(DISTINCT(lead_manager_code)) as lm,
        COUNT(DISTINCT(senior_manager_code)) as sm,
        COUNT(DISTINCT(manager_code)) as ma,
        COUNT(DISTINCT(employee_code)) as em
    FROM Employee
    GROUP BY company_code)
SELECT *
FROM Company AS c INNER JOIN cte USING(company_code)
ORDER BY company_code;

-- 서브쿼리 사용
SELECT 
    c.company_code,
    c.founder,
    t.lm,
    t.sm,
    t.ma,
    t.em
FROM Company AS c
INNER JOIN (
    SELECT 
        company_code,
        COUNT(DISTINCT lead_manager_code) AS lm,
        COUNT(DISTINCT senior_manager_code) AS sm,
        COUNT(DISTINCT manager_code) AS ma,
        COUNT(DISTINCT employee_code) AS em
    FROM Employee
    GROUP BY company_code
) AS t ON c.company_code = t.company_code
ORDER BY c.company_code;
