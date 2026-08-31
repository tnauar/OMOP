SELECT
  SUM(
    (length(lower(free_text)) - length(replace(lower(free_text), 'rokot', '')))
    / length('rokot')
  ) AS rokot_maara
FROM omop.common
WHERE lower(free_text) LIKE '%rokot%';

SELECT COUNT(id) AS rivien_maara
FROM omop.common
WHERE lower(free_text) LIKE '%rokot%';
