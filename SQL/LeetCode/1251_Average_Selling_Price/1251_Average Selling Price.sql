WITH base AS (
    SELECT
            p.product_id,
            p.start_date,
            p.end_date,
            IF(u.purchase_date BETWEEN start_date AND end_date, p.price * u.units, 0) AS value,
            u.units
    FROM Prices AS p LEFT JOIN UnitsSold AS u USING(product_id)
), sum_of_units AS (
    SELECT
        product_id,
        SUM(units) AS units_sm
    FROM UnitsSold
    GROUP BY product_id
), sum_of_value AS (
    SELECT
        product_id,
        SUM(value) AS value_sm
    FROM base
    GROUP BY product_id
)
SELECT
    product_id,
    IF(units_sm IS NULL, 0, ROUND(value_sm / units_sm, 2)) AS average_price 
FROM sum_of_value AS v LEFT JOIN sum_of_units AS u USING(product_id);

# solution
SELECT
    p.product_id,
    IFNULL(ROUND(SUM(p.price * u.units) / SUM(u.units), 2), 0) AS average_price
FROM
    Prices AS p
LEFT JOIN
    UnitsSold AS u
ON
    p.product_id = u.product_id
    AND u.purchase_date BETWEEN p.start_date AND p.end_date
GROUP BY
    p.product_id;