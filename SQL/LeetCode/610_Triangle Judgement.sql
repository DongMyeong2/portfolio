SELECT
    *,
    CASE
        WHEN x >= y AND x >= z AND x < y + z THEN 'Yes'
        WHEN y >= x AND y >= z AND y < x + z THEN 'Yes'
        WHEN z >= x AND z >= y AND z < x + y THEN 'Yes'
        ELSE 'No'
    END AS `triangle`
FROM Triangle