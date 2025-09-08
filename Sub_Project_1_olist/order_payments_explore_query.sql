# olist_order_payments 데이터셋 탐색
SHOW COLUMNS FROM order_payments;

SELECT *
FROM order_payments;

# 전체 행 수 확인 -> 103,886건
SELECT COUNT(*) AS total_cnt
FROM order_payments;

# 결측값 확인 -> 0건
SELECT *
FROM order_payments
WHERE order_id IS NULL
    OR payment_sequential IS NULL
    OR payment_type IS NULL
    OR payment_installments IS NULL
    OR payment_value IS NULL;

# 전체 중복값 확인 -> 0건
SELECT
    *,
    COUNT(*) AS cnt
FROM order_payments
GROUP BY order_id, payment_sequential, payment_type, payment_installments, payment_value
HAVING COUNT(*) > 1;

# 한 결제를 여러 결제 수단으로 나눠서 결제하는 경우 존재 2,961건
# 결제 수단: credit_card(신용카드), debit_card(체크카드), boleto(무통장입금), voucher(쿠폰, 크레딧 등), not_defined(분류 불명)
SELECT
    order_id,
    COUNT(*) AS cnt
FROM order_payments
GROUP BY order_id
HAVING COUNT(*) > 1;

# 여러 결제 수단 사용할 때, 어떤 결제 수단들을 사용하는지 확인
# 결제 수단 PIVOT하여 확인
# 여러 결제 수단 사용한 경우: 2,246건
# 전체 결제 건 수: 99,440건 (order_items와 안맞는데 order_items에 없는 경우도 있음 -> INNER JOIN하며 제거)
# 한 건(credit_card + debit_card)을 제외하고는 모두 (credit_card + voucher) 조합
WITH base AS (
    SELECT
        order_id,
        MAX(IF(payment_type="credit_card", cnt, 0)) AS credit_card,
        MAX(IF(payment_type="debit_card", cnt, 0)) AS debit_card,
        MAX(IF(payment_type="boleto", cnt, 0)) AS boleto,
        MAX(IF(payment_type="voucher", cnt, 0)) AS voucher,
        MAX(IF(payment_type="not_defined", cnt, 0)) AS not_defined
    FROM (
        SELECT
            order_id,
            payment_type,
            COUNT(*) AS `cnt`
        FROM order_payments
        GROUP BY order_id, payment_type
    ) AS pt
    GROUP BY order_id
), upper_two_payment_types AS (
    SELECT *
    FROM base
    WHERE (credit_card>0) + (debit_card>0) + (boleto>0) + (voucher>0) + (not_defined>0) >= 2
)
SELECT *
FROM upper_two_payment_types
WHERE credit_card > 0 AND voucher > 0;

# 소비자들이 주로 사용하는 결제 수단
# 신용카드 가장 많이 사용 (할부는 신용카드만 가능한 듯)
# 한 번 결제할 때 평균 가격은 비슷
SELECT
    payment_type,
    COUNT(*) AS cnt,
    AVG(payment_installments),
    SUM(payment_value),
    AVG(payment_value)
FROM order_payments
GROUP BY payment_type;

# 확인용
-- SELECT *
-- FROM order_payments
-- WHERE order_id = 'a079628ac8002126e75f86b0f87332e4';

-- SELECT *
-- FROM view_order_items
-- WHERE order_id = 'a079628ac8002126e75f86b0f87332e4';