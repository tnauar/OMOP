CREATE TABLE omop.Excel_bronze AS
SELECT *
FROM omop.Excel_raw;

ALTER TABLE omop.Excel_bronze
DROP COLUMN nationality,
DROP COLUMN education;

ALTER TABLE omop.Excel_bronze
ADD COLUMN firstname TEXT,
ADD COLUMN lastname TEXT;

UPDATE omop.Excel_bronze
SET
firstname = split_part(trim(name),' ',1),
lastname = split_part(trim(name),' ',2);

ALTER TABLE omop.Excel_bronze
DROP COLUMN name;
