SELECT E.name, B.bonus
FROM Employee AS E LEFT JOIN Bonus AS B USING(empID)
WHERE B.bonus < 1000 OR B.bonus IS NULL;