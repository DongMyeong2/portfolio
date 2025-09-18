# olist_orders 데이터셋 탐색
SHOW COLUMNS FROM orders;

# 전체 행 수 확인 -> 99,441건
SELECT COUNT(*) AS total_cnt
FROM orders;

SELECT *
FROM orders;

# 결측값 확인 -> 2,980건
# order_state에 따라 결측값 존재
SELECT *
FROM orders
WHERE order_status = ''
    OR order_purchase_timestamp = ''
    OR order_approved_at = ''
    OR order_delivered_carrier_date = ''
    OR order_delivered_customer_date = ''
    OR order_estimated_delivery_date = '';

# 데이터 수집기간
# 2016년 9월 4일 ~ 2018년 10월 17일
SELECT
    MAX(STR_TO_DATE(TRIM(order_purchase_timestamp), '%Y-%m-%d %H:%i:%s')) AS max_date,
    MIN(STR_TO_DATE(TRIM(order_purchase_timestamp), '%Y-%m-%d %H:%i:%s')) AS min_date
FROM orders;

# 전체 중복값 확인 -> 0건
SELECT
    *,
    COUNT(*) AS cnt
FROM orders
GROUP BY order_id, customer_id, order_status, order_purchase_timestamp, order_approved_at,
    order_delivered_carrier_date, order_delivered_customer_date, order_estimated_delivery_date
HAVING COUNT(*) > 1;

# 주문 상태 확인
# delivered(96,478건): 상품을 고객이 수령한 상태
# shipped(1,107건): 배송 중
# canceled(625건): 결제 미승인, 고객 취소, 사후 환불 등 다양한 이유로 주문 취소
# unavailable(609건): 재고/주소/제휴 문제 등으로 판매 불가 처리
# invoiced(314건): 브라질 전자 세금 계산서 발행 단계로 "출고 준비 완료"로 인지
# processing(301건): 판매자가 상품을 준비/포장 중
# created(5건): 주문이 생성된 직후. 결제 승인 전 단계
# approved(2건): 결제 승인 상태. 포장 전
SELECT
    order_status,
    COUNT(*)
FROM orders
GROUP BY order_status;

# CREATE OR REPLACE VIEW olist.view_orders AS
WITH delivered_order AS (
    SELECT *
    FROM orders
    WHERE order_status = 'delivered'
)
SELECT *
FROM delivered_order;

# 결제 승인까지 걸리는 평균 시간 -> 약 10시간
WITH base AS (
  SELECT
    STR_TO_DATE(TRIM(order_purchase_timestamp), '%Y-%m-%d %H:%i:%s') AS purchase_ts,
    STR_TO_DATE(TRIM(order_approved_at), '%Y-%m-%d %H:%i:%s') AS approved_ts
  FROM view_orders
)
SELECT
  AVG(TIMESTAMPDIFF(SECOND, purchase_ts, approved_ts)) / 3600 AS avg_hours
FROM base
WHERE approved_ts IS NOT NULL
  AND approved_ts >= purchase_ts;

# 출고까지 걸리는 평균 시간 -> 약 68시간
WITH base AS (
  SELECT
    STR_TO_DATE(TRIM(order_approved_at), '%Y-%m-%d %H:%i:%s') AS approved_ts,
    STR_TO_DATE(TRIM(order_delivered_carrier_date), '%Y-%m-%d %H:%i:%s') AS delivered_carrier_ts
  FROM view_orders
)
SELECT
  AVG(TIMESTAMPDIFF(SECOND, approved_ts, delivered_carrier_ts)) / 3600 AS avg_hours
FROM base
WHERE delivered_carrier_ts >= approved_ts;

# 고객 수령까지 걸리는 평균 시간 -> 약 223시간
WITH base AS (
  SELECT
    STR_TO_DATE(TRIM(order_delivered_carrier_date), '%Y-%m-%d %H:%i:%s') AS delivered_carrier_ts,
    STR_TO_DATE(TRIM(order_delivered_customer_date), '%Y-%m-%d %H:%i:%s') AS delivered_customer_ts
  FROM view_orders
)
SELECT
  AVG(TIMESTAMPDIFF(SECOND, delivered_carrier_ts, delivered_customer_ts)) / 3600 AS avg_hours
FROM base
WHERE delivered_customer_ts >= delivered_carrier_ts;

# 고객 수령까지 예상 평균 시간 -> 약 495시간
WITH base AS (
  SELECT
    STR_TO_DATE(TRIM(order_delivered_carrier_date), '%Y-%m-%d %H:%i:%s') AS delivered_carrier_ts,
    STR_TO_DATE(TRIM(order_estimated_delivery_date), '%Y-%m-%d %H:%i:%s') AS estimated_delivery_ts
  FROM view_orders
)
SELECT
  AVG(TIMESTAMPDIFF(SECOND, delivered_carrier_ts, estimated_delivery_ts)) / 3600 AS avg_hours
FROM base
WHERE estimated_delivery_ts >= delivered_carrier_ts;

# 실제 배송 시간과 예상 배송 시간의 차이 -> 약 270시간
WITH base AS (
  SELECT
    STR_TO_DATE(TRIM(order_delivered_carrier_date), '%Y-%m-%d %H:%i:%s') AS delivered_carrier_ts,
    STR_TO_DATE(TRIM(order_delivered_customer_date), '%Y-%m-%d %H:%i:%s') AS delivered_customer_ts,
    STR_TO_DATE(TRIM(order_estimated_delivery_date), '%Y-%m-%d %H:%i:%s') AS estimated_delivery_ts
  FROM view_orders
), cal AS (
    SELECT
    TIMESTAMPDIFF(SECOND, delivered_carrier_ts, delivered_customer_ts) / 3600 AS delivered_hours,
    TIMESTAMPDIFF(SECOND, delivered_carrier_ts, estimated_delivery_ts) / 3600 AS estimated_hours
    FROM base
    WHERE estimated_delivery_ts >= delivered_carrier_ts AND delivered_customer_ts >= delivered_carrier_ts
)
SELECT AVG(estimated_hours - delivered_hours)
FROM cal;