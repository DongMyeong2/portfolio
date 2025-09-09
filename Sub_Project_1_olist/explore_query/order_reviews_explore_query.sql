# olist_order_reviews 데이터셋 탐색
SHOW COLUMNS FROM order_reviews;

# 전체 행 수 확인 -> 99,204건
# 유효한 order_id 수: 98,653건 
SELECT *
FROM order_reviews;

# 결측값 확인 -> 89,374건
# 제목과 내용이 결측이라 review_score만 이용
SELECT *
FROM order_reviews
WHERE review_id = ''
    OR order_id = ''
    OR review_score = ''
    OR review_comment_title = ''
    OR review_comment_message = ''
    OR review_creation_date = ''
    OR review_answer_timestamp = '';

# 전체 중복값 확인 -> 0건
SELECT
    *,
    COUNT(*) AS cnt
FROM order_reviews
GROUP BY review_id, order_id, review_score, review_comment_title, review_comment_message, review_creation_date, review_answer_timestamp
HAVING COUNT(*) > 1;

# 한 order_id에 여러 review가 달림 -> 한 주문에 여러 상품을 주문한 경우인가 했지만 아님
# 어떤 리뷰를 남겨야할까
WITH ac AS (
    SELECT
        order_id
    FROM order_reviews
    GROUP BY order_id
    HAVING COUNT(*) > 1
    LIMIT 10
)
SELECT *
FROM order_reviews
WHERE order_id IN (SELECT order_id FROM ac)
ORDER BY order_id;

# 리뷰 점수 확인
# 대체로 높은 편
SELECT AVG(review_score)
FROM order_reviews;

# 리뷰 생성 날짜와 리뷰 작성 날짜가 이상한 경우: 70건
# 리뷰 생성 전에 리뷰 작성이 일어난 경우는 없음
WITH clean AS (
    SELECT *
    FROM order_reviews
    WHERE NULLIF(TRIM(review_creation_date), '') IS NOT NULL
        AND NULLIF(TRIM(review_answer_timestamp), '') IS NOT NULL
        AND STR_TO_DATE(TRIM(review_creation_date), '%Y-%m-%d %H:%i:%s') IS NOT NULL
        AND STR_TO_DATE(TRIM(review_answer_timestamp), '%Y-%m-%d %H:%i:%s') IS NOT NULL
)
SELECT *
FROM clean
WHERE STR_TO_DATE(TRIM(review_creation_date), '%Y-%m-%d %H:%i:%s') > STR_TO_DATE(TRIM(review_answer_timestamp), '%Y-%m-%d %H:%i:%s');