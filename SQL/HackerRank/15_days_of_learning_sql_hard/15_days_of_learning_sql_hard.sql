SELECT
  d.submission_date,
  COUNT(*) AS unique_daily_submitters,
  best.hacker_id,
  h.name
FROM (
    SELECT
        DISTINCT
            submission_date,
            hacker_id
   FROM Submissions
    ) AS s1
    JOIN (
        SELECT
            t.submission_date,
            MIN(t.hacker_id) AS hacker_id
        FROM (
          SELECT
            submission_date,
            hacker_id,
            COUNT(*) AS cnt
          FROM Submissions
          GROUP BY submission_date, hacker_id
        ) t
        JOIN (
          SELECT
            submission_date,
            MAX(cnt) AS maxcnt
          FROM (
            SELECT
              submission_date,
              hacker_id,
              COUNT(*) AS cnt
            FROM Submissions
            GROUP BY submission_date, hacker_id
            ) x
          GROUP BY submission_date
        ) m
        ON t.submission_date = m.submission_date AND t.cnt = m.maxcnt
        GROUP BY t.submission_date
    ) best
    ON best.submission_date = s1.submission_date
    JOIN Hackers h
    ON h.hacker_id = best.hacker_id
    JOIN (
        SELECT
            DISTINCT
                submission_date
        FROM Submissions) d
    ON d.submission_date = s1.submission_date
WHERE
  NOT EXISTS (
    SELECT 1
    FROM (
        SELECT
          DISTINCT
            submission_date
        FROM Submissions
        ) cal
    WHERE cal.submission_date <= s1.submission_date
      AND NOT EXISTS (
        SELECT 1
        FROM Submissions s2
        WHERE s2.hacker_id = s1.hacker_id AND s2.submission_date = cal.submission_date
      )
  )
GROUP BY d.submission_date, best.hacker_id, h.name
ORDER BY d.submission_date;
