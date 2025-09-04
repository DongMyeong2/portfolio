-- case 1
SELECT DISTINCT(CITY)
FROM STATION
WHERE SUBSTRING(CITY, 1, 1) IN ('a', 'e', 'i', 'o', 'u');

-- case 2
SELECT DISTINCT(CITY)
FROM STATION
WHERE LEFT(CITY, 1) IN ('a', 'e', 'i', 'o', 'u');
