WITH ex AS (
    SELECT
        student_id,
        subject_name,
        COUNT(*) AS `attended_exams`
    FROM Examinations
    GROUP BY student_id, subject_name
)

SELECT
    c.student_id ,
    c.student_name,
    c.subject_name,
    COALESCE(ex.attended_exams, 0) AS `attended_exams`
FROM (SELECT * FROM Students AS st CROSS JOIN Subjects AS sb) AS c
    LEFT JOIN ex ON c.student_id = ex.student_id AND c.subject_name = ex.subject_name
ORDER BY student_id, subject_name;