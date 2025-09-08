# olist_sellers 데이터셋 탐색
SHOW COLUMNS FROM sellers;

# 전체 행 수 확인 -> 3,095건
SELECT COUNT(*) AS total_cnt
FROM sellers;

SELECT *
FROM sellers;

# 결측값 확인 -> 0건
SELECT *
FROM sellers
WHERE seller_id IS NULL
    OR seller_zip_code_prefix IS NULL
    OR seller_city IS NULL
    OR seller_state IS NULL;

# 전체 중복값 확인 -> 0건
SELECT
    *,
    COUNT(*) AS cnt
FROM sellers
GROUP BY seller_id, seller_zip_code_prefix, seller_city, seller_state
HAVING COUNT(*) > 1;

# 가장 많은 판매자가 있는 주
SELECT
    seller_state,
    COUNT(*) AS state_cnt
FROM sellers
GROUP BY seller_state
ORDER BY state_cnt DESC;

# 가장 많은 판매자가 있는 주가 전체에서 차지하는 비율
# SP(상파울루) 주가 전체 60%
# PR(파라나주) 주가 전체 11%
# MG(미나스제라이스) 주가 전체 8%
# 나머지 주들은 6% 이하
SELECT
    *,
    CONCAT(ROUND(state_cnt/total_cnt, 2), '%') AS state_ratio
FROM (
    SELECT
        seller_state,
        COUNT(*) AS state_cnt,
        (SELECT COUNT(*) FROM sellers) AS total_cnt
    FROM sellers
    GROUP BY seller_state
    ORDER BY state_cnt DESC
) AS seller_cnt;

# 가장 많은 판매자가 있는 도시
SELECT
    seller_city,
    seller_state,
    COUNT(*) AS city_cnt
FROM sellers
GROUP BY seller_city, seller_state
ORDER BY city_cnt DESC;

# 가장 많은 소비자가 있는 도시가 전체에서 차지하는 비율
# SP 주의 상파울루가 22%로 가장 큰 비중 차지
# 상파울루 도시의 고객이 두 번째로 많은 고객이 있는 PR 주보다 그 수가 많음
SELECT
    *,
    CONCAT(ROUND(city_cnt/total_cnt, 2), '%') AS city_ratio
FROM (
    SELECT
        seller_city,
        seller_state,
        COUNT(*) AS city_cnt,
        (SELECT COUNT(*) FROM sellers) AS total_cnt
    FROM sellers
    GROUP BY seller_city, seller_state
    ORDER BY city_cnt DESC
) AS customer_cnt;