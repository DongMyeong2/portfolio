WITH base AS (
  SELECT
    company_id,
    title
  FROM job_listings
  GROUP BY company_id, title
  HAVING COUNT(*) > 1
)

SELECT COUNT(*) AS duplicate_companies
FROM base;