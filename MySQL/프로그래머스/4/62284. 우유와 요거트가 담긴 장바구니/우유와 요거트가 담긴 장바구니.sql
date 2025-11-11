WITH base AS (
    SELECT
        DISTINCT
            CART_ID,
            NAME
    FROM CART_PRODUCTS
)
SELECT
    CART_ID
FROM (
    SELECT
        CART_ID,
        NAME,
        IF(NAME IN ('Milk', 'Yogurt'), 1, 0) AS ck
    FROM base) AS a
GROUP BY CART_ID
HAVING SUM(ck) >= 2
ORDER BY CART_ID