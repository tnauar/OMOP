CREATE TABLE omop.JSON_bronze AS
SELECT *
FROM omop.JSON_raw;

ALTER TABLE omop.JSON_bronze
ADD COLUMN firstname TEXT,
ADD COLUMN lastname TEXT;

UPDATE omop.JSON_bronze
SET
firstname = split_part(trim(name),' ',1),
lastname = split_part(trim(name),' ',2);

ALTER TABLE omop.JSON_bronze
DROP COLUMN name;
