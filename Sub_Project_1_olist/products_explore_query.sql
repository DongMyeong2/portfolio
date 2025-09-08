# olist_products 데이터셋 탐색
SHOW COLUMNS FROM products;

# 전체 행 수 확인 -> 32,340건
SELECT COUNT(*) AS total_cnt
FROM products;

SELECT *
FROM products;

# 결측값 확인 -> 0건
SELECT *
FROM products
WHERE product_id IS NULL
    OR product_category_name IS NULL
    OR product_name_lenght IS NULL
    OR product_description_lenght IS NULL
    OR product_photos_qty IS NULL
    OR product_weight_g IS NULL
    OR product_length_cm IS NULL
    OR product_height_cm IS NULL
    OR product_width_cm IS NULL;

# 전체 중복값 확인 -> 0건
SELECT
    *,
    COUNT(*) AS cnt
FROM products
GROUP BY product_id, product_category_name, product_name_lenght, product_description_lenght, product_photos_qty,
    product_weight_g, product_length_cm, product_height_cm, product_width_cm
HAVING COUNT(*) > 1;

# 판매하고 있는 상품 카테고리
SELECT n.product_category_name_english, COUNT(*)
FROM products AS p INNER JOIN product_category_name_translation AS n USING(product_category_name)
GROUP BY n.product_category_name_english
ORDER BY COUNT(*) DESC;