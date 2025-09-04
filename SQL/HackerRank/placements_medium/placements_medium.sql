WITH Students_Salary AS (
    SELECT
        S.ID,
        S.Name AS my_name,
        P.Salary AS my_salary
    FROM Students AS S LEFT JOIN Packages AS P USING(ID)
), Freiends_Salary AS (
    SELECT
        F_info.ID,
        F_info.Name AS friend_name,
        P.Salary AS friend_salary
    FROM (
        SELECT
            F.ID,
            F.Friend_ID,
            S.Name
        FROM Friends As F LEFT JOIN Students AS S ON F.Friend_ID = S.ID    
    ) AS F_info LEFT JOIN Packages AS P ON F_info.Friend_ID = P.ID
)
SELECT S.my_name
FROM Students_Salary AS S LEFT JOIN Freiends_Salary AS F USING(ID)
WHERE my_salary < friend_salary
ORDER BY friend_salary;
