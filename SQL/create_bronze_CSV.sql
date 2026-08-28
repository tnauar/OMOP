CREATE TABLE omop.CSV_bronze AS
SELECT *
FROM omop.CSV_raw;

ALTER TABLE omop.CSV_bronze
DROP COLUMN healthcare_plan;

ALTER TABLE omop.CSV_bronze
ADD COLUMN firstname TEXT,
ADD COLUMN lastname TEXT;

UPDATE omop.CSV_bronze
SET
firstname = split_part(trim(name),' ',1),
lastname = split_part(trim(name),' ',2);

ALTER TABLE omop.CSV_bronze
DROP COLUMN name;
