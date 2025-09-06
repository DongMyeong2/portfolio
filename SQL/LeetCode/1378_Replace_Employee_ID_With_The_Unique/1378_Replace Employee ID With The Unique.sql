SELECT unique_id, name
FROM Employees AS E LEFT JOIN EmployeeUNI AS U USING(id);