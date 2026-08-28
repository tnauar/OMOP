CREATE TABLE omop.Excel_raw (
        row_id SERIAL PRIMARY KEY,
        visit_index INTEGER,
        person_id INTEGER,
	nationality TEXT,
	education TEXT,
        name TEXT,
        gender CHAR,
        age INTEGER,
        visit_date DATE,
        visit_type TEXT,
        visit_id INTEGER,
        condition TEXT,
        duration TEXT,
        symptom_1 TEXT,
        symptom_2 TEXT,
        medication TEXT,
        free_text TEXT
);
