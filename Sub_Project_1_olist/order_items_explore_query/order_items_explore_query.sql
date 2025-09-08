# olist_order_items 데이터셋 탐색
SHOW COLUMNS FROM order_items;

# 전체 행 수 확인 -> 112,650건
# 유효한 order_id 수: 98,666건 
SELECT COUNT(*) AS total_cnt
FROM order_items;

# 결측값 확인 -> 0건
SELECT *
FROM order_items
WHERE order_id IS NULL
    OR order_item_id IS NULL
    OR product_id IS NULL
    OR seller_id IS NULL
    OR shipping_limit_date IS NULL
    OR price IS NULL
    OR freight_value IS NULL;

# 전체 중복값 확인 -> 0건
SELECT
    order_id, order_item_id, product_id, seller_id, shipping_limit_date, price, freight_value,
    COUNT(*) AS cnt
FROM order_items
GROUP BY order_id, order_item_id, product_id, seller_id, shipping_limit_date, price, freight_value
HAVING COUNT(*) > 1;


# 상품별 중복값 확인 -> 7,088건
# 같은 상품을 여러 번 시킨 경우 그 개수만큼 행이 하나씩 생김
# order_payments를 통해 확인해본 결과, 같은 상품을 여러 번 시킨 경우로 판단
# 배송비도 상품 수만큼 여러 번 부과
SELECT
    order_id, product_id, seller_id, shipping_limit_date, price, freight_value,
    COUNT(*) AS cnt
FROM order_items
GROUP BY order_id, product_id, seller_id, shipping_limit_date, price, freight_value
HAVING COUNT(*) > 1
ORDER BY cnt DESC;

# 한 번의 주문에 여러 상품을 시킨 경우도 존재 -> 3,236건
# 가장 다양하게 상품을 주문한 경우 -> 8개의 각기 다른 상품을 주문
# order_id = 'ca3625898fbd48669d50701aba51cd5f'
SELECT
    order_id,
    COUNT(*) AS cnt
FROM (
    SELECT order_id, product_id, seller_id
    FROM order_items
    GROUP BY order_id, product_id, seller_id
) AS c
GROUP BY order_id
HAVING COUNT(*) > 1
ORDER BY cnt DESC;

# 여러 행으로 표현하지말고 하나의 행으로 표현
# view로 만들어서 계속 사용
# CREATE OR REPLACE VIEW olist.view_order_items AS
SELECT
    order_id,
    product_id,
    seller_id,
    shipping_limit_date,
    price,
    freight_value,
    COUNT(*) AS order_count
FROM order_items
GROUP BY order_id, product_id, seller_id, shipping_limit_date, price, freight_value;

# 가장 큰 요금이 발생한 주문 순서대로
SELECT order_id, SUM(each_price) AS total_price
FROM (
    SELECT order_id, (price + freight_value) * order_count AS each_price
    FROM view_order_items
) AS cal
GROUP BY order_id
ORDER BY total_price DESC;

# 판매자들의 판매 수익
# 판매자 최고 수익: 249,640
# 판매자 최저 수익: 12
# 판매자 평균 수익: 5,119
SELECT seller_id, SUM(each_price) AS total_price
FROM (
    SELECT seller_id, (price + freight_value) * order_count AS each_price
    FROM view_order_items
) AS cal
GROUP BY seller_id
ORDER BY total_price DESC;

# 상품과 판매자의 관계
# 한 product_id에 여러 판매자가 있을 수 있음
# 가장 다양한 판매자들이 파는 상품 -> 8건
# 판매자에 따라 상품 가격과 배송비가 다름
# 5명 이상의 판매자가 판매하는 상품들의 카테고리 분포
# computers_accessories: 7건
# watches_gifts: 7건
# health_beauty: 1건
# perfumery: 1건
WITH check_relation_of_products_and_sellers AS (
    SELECT
        product_id,
        COUNT(*) AS product_cnt
    FROM (
        SELECT 
            DISTINCT
                seller_id,
                product_id
        FROM view_order_items
    ) AS p
    GROUP BY product_id
    HAVING COUNT(*) > 1
    ORDER BY product_cnt DESC
), top10_picked_product AS (
    SELECT product_id
    FROM check_relation_of_products_and_sellers
    WHERE product_cnt >= 5
)
SELECT
    n.product_category_name_english,
    COUNT(*) AS product_category_cnt
FROM products AS p INNER JOIN product_category_name_translation AS n USING(product_category_name)
WHERE p.product_id IN (SELECT * FROM top10_picked_product)
GROUP BY n.product_category_name_english
ORDER BY product_category_cnt DESC;

# 상품 평균 가격
# 가장 비싼 상품 판매가: 6,735
# 가장 싼  상품 판매가: 0.85
SELECT product_id, AVG(price), AVG(freight_value)
FROM view_order_items
GROUP BY product_id
ORDER BY AVG(price) DESC;

# 상품 수익
# 가장 많은 수익은 낸 10개의 상품 가격 분포는 다양함(71 ~ 1397 사이)
WITH sell_profit AS (
    SELECT product_id, SUM(each_price) AS total_price
    FROM (
        SELECT product_id, (price + freight_value) * order_count AS each_price
        FROM view_order_items
    ) AS cal
    GROUP BY product_id
    ORDER BY total_price DESC
), top10_profit_product AS (
    SELECT product_id
    FROM sell_profit
    LIMIT 10
)
SELECT product_id, AVG(price), SUM(order_count)
FROM view_order_items
WHERE product_id IN (SELECT * FROM top10_profit_product)
GROUP BY product_id;

# 상품 판매 횟수
SELECT product_id, AVG(price), COUNT(*)
FROM view_order_items
GROUP BY product_id
ORDER BY COUNT(*) DESC;

# 총 상품 판매 횟수
SELECT product_id, AVG(price), SUM(order_count)
FROM view_order_items
GROUP BY product_id
ORDER BY SUM(order_count) DESC;

# 한 번에 여러 번 주문하는 상품들의 가격 분포
# 가격대 다양하게 분포
SELECT order_count, AVG(price)
FROM view_order_items
WHERE order_count > 1
GROUP BY order_count
ORDER BY order_count;