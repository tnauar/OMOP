CREATE TABLE omop.RDS_bronze AS
SELECT *
FROM omop.RDS_raw;

ALTER TABLE omop.RDS_bronze
DROP COLUMN nationality,
DROP COLUMN education,
DROP COLUMN healthcare_plan;

