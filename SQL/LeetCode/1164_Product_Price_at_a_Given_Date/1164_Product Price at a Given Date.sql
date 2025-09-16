WITH base AS (
    SELECT
        DISTINCT product_id,
        10 AS price
    FROM Products
), new_price AS (
    SELECT
        product_id,
        price
    FROM (
        SELECT
            product_id,
            new_price,
            FIRST_VALUE(new_price) OVER (PARTITION BY product_id ORDER BY change_date DESC) AS price
        FROM Products
        WHERE change_date <= '2019-08-16'
    ) AS p
    WHERE new_price = price
)
SELECT
    DISTINCT
        b.product_id,
        COALESCE(p.price, b.price) AS price
FROM base AS b LEFT JOIN new_price AS p USING(product_id);