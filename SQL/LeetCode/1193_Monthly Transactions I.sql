WITH base AS (
    SELECT
        id,
        LEFT(trans_date, 7) AS month,
        country,
        state,
        amount
    FROM Transactions
), total_trans AS (
    SELECT
        month,
        country,
        COUNT(state) AS trans_count,
        SUM(amount) AS trans_total_amount
    FROM base
    GROUP BY month, country
), approved_trans AS (
    SELECT
        month,
        country,
        COUNT(state) AS approved_count,
        SUM(amount) AS approved_total_amount
    FROM base
    WHERE state = 'approved'
    GROUP BY month, country
)
SELECT
    t.month,
    t.country,
    t.trans_count,
    COALESCE(a.approved_count, 0) AS approved_count,
    t.trans_total_amount,
    COALESCE(a.approved_total_amount, 0) AS approved_total_amount
FROM total_trans AS t LEFT JOIN approved_trans AS a ON t.month = a.month AND (t.country <=> a.country);

# solution
SELECT 
    LEFT(trans_date, 7) AS month,
    country, 
    COUNT(id) AS trans_count,
    SUM(state = 'approved') AS approved_count,
    SUM(amount) AS trans_total_amount,
    SUM((state = 'approved') * amount) AS approved_total_amount
FROM 
    Transactions
GROUP BY 
    month, country;