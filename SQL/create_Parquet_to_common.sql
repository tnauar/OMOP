INSERT INTO omop.common (id, visit_index, visit_type, visit_id, visit_date, person_id,
			gender, age, symptom_1, symptom_2, medication, condition,
			duration, free_text, firstname, lastname)
SELECT 
	row_id + 3000,
	visit_index + 30000,
	visit_type,
	visit_id,
        visit_date,
	person_id + 30000,
	gender,
	age,
	symptom_1,
	symptom_2,
	medication,
	condition,
	duration,
	free_text,
	firstname,
	lastname

FROM omop.Parquet_silver;
