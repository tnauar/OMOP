CREATE TABLE omop.RDS_raw (
        row_id SERIAL PRIMARY KEY,
	gender CHAR,
	firstname TEXT,
	lastname TEXT,
        condition TEXT,
        duration TEXT,
	education TEXT,
	healthcare_plan TEXT,
        medication TEXT,
	nationality TEXT,
        symptom_1 TEXT,
        symptom_2 TEXT,
        free_text TEXT,
	visit_index INTEGER,
        person_id INTEGER,
        age INTEGER,
        visit_id INTEGER,
        visit_type TEXT,
        visit_date DATE
);

