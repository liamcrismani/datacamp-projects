-- select fields
SELECT stay, 
COUNT(*) AS count_int,
ROUND(AVG(todep::numeric), 2) AS average_phq,
ROUND(AVG(tosc::numeric), 2) AS average_scs,
ROUND(AVG(toas::numeric), 2) AS average_as
FROM students 
-- ensure only international students
WHERE inter_dom = 'Inter'
-- Group by length of stay
GROUP BY stay
-- order by length of stay
ORDER by stay DESC;