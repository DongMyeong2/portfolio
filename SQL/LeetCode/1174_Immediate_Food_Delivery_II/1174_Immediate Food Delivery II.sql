WITH base AS (
    SELECT
        customer_id,
        IF(DATEDIFF(customer_pref_delivery_date, order_date) = 0, 1, 0) AS `order`
    FROM (
        SELECT
            customer_id,
            order_date,
            FIRST_VALUE(order_date) OVER (PARTITION BY customer_id ORDER BY order_date) AS first_order,
            customer_pref_delivery_date
        FROM Delivery
    ) AS d
    WHERE order_date = first_order
)
SELECT
    ROUND((SUM(`order`) / COUNT(`order`)) * 100, 2) AS immediate_percentage
FROM base;