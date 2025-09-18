# olist_customers 데이터셋 탐색
SHOW COLUMNS FROM customers;

# 전체 행 수 확인 -> 99,441건
SELECT COUNT(*) AS total_cnt
FROM customers;

# 결측값 확인 -> 0건
SELECT *
FROM customers
WHERE customer_id IS NULL
    OR customer_unique_id IS NULL
    OR customer_city IS NULL
    OR customer_state IS NULL;

# 전체 중복값 확인 -> 0건
SELECT
    *,
    COUNT(*) AS cnt
FROM customers
GROUP BY customer_id, customer_unique_id, customer_zip_code_prefix, customer_city, customer_state
HAVING COUNT(*) > 1;

# 유니크한 고객 ID 중복 확인 -> 중복 존재 -> orders의 customer_id를 바꿀 필요 있음
SELECT
    customer_unique_id,
    COUNT(*) AS cnt
FROM customers
GROUP BY customer_unique_id
HAVING COUNT(*) > 1;

# 가장 많은 소비자가 있는 주
SELECT
    customer_state,
    COUNT(*) AS state_cnt
FROM customers
GROUP BY customer_state
ORDER BY state_cnt DESC;

# 가장 많은 소비자가 있는 주가 전체에서 차지하는 비율
# SP(상파울루) 주가 전체 42%
# RJ(리우데자네이루) 주가 전체 13%
# MG(미나스제라이스) 주가 전체 12%
# 나머지 주들은 5% 이하
SELECT
    *,
    CONCAT(ROUND(state_cnt/total_cnt, 2), '%') AS state_ratio
FROM (
    SELECT
        customer_state,
        COUNT(*) AS state_cnt,
        (SELECT COUNT(*) FROM customers) AS total_cnt
    FROM customers
    GROUP BY customer_state
    ORDER BY state_cnt DESC
) AS customer_cnt;

# 가장 많은 소비자가 있는 도시
SELECT
    customer_city,
    customer_state,
    COUNT(*) AS city_cnt
FROM customers
GROUP BY customer_city, customer_state
ORDER BY city_cnt DESC;

# 가장 많은 소비자가 있는 도시가 전체에서 차지하는 비율
# SP 주의 상파울루가 16%로 가장 큰 비중 차지
# 상파울루 도시의 고객이 두 번째로 많은 고객이 있는 RJ 주보다 그 수가 많음
SELECT
    *,
    CONCAT(ROUND(city_cnt/total_cnt, 2), '%') AS city_ratio
FROM (
    SELECT
        customer_city,
        customer_state,
        COUNT(*) AS city_cnt,
        (SELECT COUNT(*) FROM customers) AS total_cnt
    FROM customers
    GROUP BY customer_city, customer_state
    ORDER BY city_cnt DESC
) AS customer_cnt;