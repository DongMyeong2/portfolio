WITH total_cnt AS (
    SELECT 
        user_id,
        COUNT(*) AS `cnt`
    FROM Confirmations
    GROUP BY user_id
), conf_cnt AS (
    SELECT
        user_id,
        COUNT(*) AS `cnt`
    FROM Confirmations
    WHERE action = 'confirmed'
    GROUP BY user_id
)

SELECT
    user_id,
    ROUND(IF(total_cnt = 0, 0, conf_cnt/total_cnt), 2) AS confirmation_rate
FROM (
    SELECT
        s.user_id,
        IFNULL(c.cnt, 0) AS conf_cnt,
        IFNULL(t.cnt, 0) AS total_cnt
    FROM Signups AS s
        LEFT JOIN total_cnt AS t ON s.user_id = t.user_id
        LEFT JOIN conf_cnt AS c ON s.user_id = c.user_id
) AS final