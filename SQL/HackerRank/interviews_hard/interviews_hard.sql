SELECT
    Contests.contest_id,
    Contests.hacker_id,
    Contests.name,
    SUM(info.sum_of_total_submissions),
    SUM(info.sum_of_total_accepted_submissions),
    SUM(info.sum_of_total_views),
    SUM(info.sum_of_total_unique_views)
FROM Contests
    LEFT JOIN Colleges ON Contests.contest_id = Colleges.contest_id
    LEFT JOIN (
        SELECT
            C.college_id,
            IFNULL(SUM(sum_of_total_views), 0) AS sum_of_total_views,
            IFNULL(SUM(sum_of_total_unique_views), 0) AS sum_of_total_unique_views,
            IFNULL(SUM(sum_of_total_submissions), 0) AS sum_of_total_submissions,
            IFNULL(SUM(sum_of_total_accepted_submissions), 0) AS sum_of_total_accepted_submissions
        FROM Challenges AS C
            LEFT JOIN (
                SELECT
                    challenge_id,
                    SUM(total_views) AS sum_of_total_views,
                    SUM(total_unique_views) AS sum_of_total_unique_views
                FROM View_Stats
                GROUP BY challenge_id
            ) AS V ON C.challenge_id = V.challenge_id
            LEFT JOIN (
                SELECT
                    challenge_id,
                    SUM(total_submissions) AS sum_of_total_submissions,
                    SUM(total_accepted_submissions) AS sum_of_total_accepted_submissions
                FROM Submission_Stats
                GROUP BY challenge_id
            ) AS S ON C.challenge_id = S.challenge_id
        GROUP BY C.college_id
    ) AS info ON Colleges.college_id = info.college_id
WHERE NOT (
    info.sum_of_total_submissions = 0
    AND info.sum_of_total_accepted_submissions = 0
    AND info.sum_of_total_views = 0
    AND info.sum_of_total_unique_views = 0
)
GROUP BY Contests.contest_id, Contests.hacker_id, Contests.name
ORDER BY Contests.contest_id;
