SELECT page_id
FROM pages AS p LEFT JOIN page_likes AS l USING(page_id)
WHERE liked_date IS NULL;