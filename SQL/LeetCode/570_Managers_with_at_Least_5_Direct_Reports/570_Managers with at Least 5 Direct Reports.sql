SELECT E.name
FROM Employee AS E
    INNER JOIN (
        SELECT
            managerId,
            COUNT(*) AS cnt
        FROM Employee
        GROUP BY managerId
        HAVING COUNT(*) >= 5
    ) AS C ON E.id = C.managerId;