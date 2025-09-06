WITH base AS (
    SELECT
        machine_id,
        process_id,
        LAG(timestamp) OVER (PARTITION BY machine_id, process_id ORDER BY `timestamp`) AS start_timestamp,
        timestamp AS end_timestamp
    FROM Activity
), cal_processing_time AS (
    SELECT
        *,
        end_timestamp - start_timestamp AS `diff_of_process`
    FROM base
    WHERE start_timestamp IS NOT NULL
)

SELECT
    machine_id,
    ROUND(AVG(diff_of_process), 3) AS processing_time
FROM cal_processing_time
GROUP BY machine_id;