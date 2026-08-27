CREATE TABLE omop.common (
	id SERIAL PRIMARY KEY,
	visit_index INTEGER,
	visit_type TEXT,
	visit_id INTEGER,
	visit_date DATE,
	person_id INTEGER,
	gender CHAR,
	age INTEGER,
	symptom_1 TEXT,
	symptom_2 TEXT,
	medication TEXT,
	condition TEXT,
	duration TEXT,
	free_text TEXT
);
