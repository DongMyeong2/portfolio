SELECT
    hacker_id,
    name,
    SUM(score) AS sum_score
FROM (
    SELECT
        S.hacker_id,
        H.name,
        S.challenge_id,
        MAX(score) AS score
    FROM Submissions AS S LEFT JOIN Hackers AS H USING(hacker_id)
    GROUP BY S.hacker_id, H.name, S.challenge_id
    ) AS base
GROUP BY hacker_id, name
HAVING SUM(score) > 0
ORDER BY sum_score DESC, hacker_id;
