WITH base1 AS (
  SELECT
    account_id,
    transaction_type,
    SUM(amount) AS amount
  FROM transactions
  GROUP BY account_id, transaction_type
), base2 AS (
  SELECT
    account_id,
    SUM(deposit) AS sum_deposit,
    SUM(withdrawal) AS sum_withdrawal
  FROM (
    SELECT
      account_id,
      CASE WHEN transaction_type = 'Deposit' THEN amount ELSE NULL END AS Deposit,
      CASE WHEN transaction_type = 'Withdrawal' THEN amount ELSE NULL END AS Withdrawal
    FROM base1
  ) AS b
  GROUP BY account_id
)

SELECT
  account_id,
  sum_deposit - sum_withdrawal AS final_balance
FROM base2;