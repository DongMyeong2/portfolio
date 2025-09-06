SELECT p.product_name, s.year, s.price
FROM Sales AS S LEFT JOIN Product AS p USING(product_id);