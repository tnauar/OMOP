CREATE TABLE omop.Parquet_bronze AS
SELECT *
FROM omop.Parquet_raw;

ALTER TABLE omop.Parquet_bronze
DROP COLUMN nationality,
DROP COLUMN education,
DROP COLUMN healthcare_plan;

ALTER TABLE omop.Parquet_bronze
ADD COLUMN firstname TEXT,
ADD COLUMN lastname TEXT;

UPDATE omop.Parquet_bronze
SET
firstname = split_part(trim(name),' ',1),
lastname = split_part(trim(name),' ',2);

ALTER TABLE omop.Parquet_bronze
DROP COLUMN name;
