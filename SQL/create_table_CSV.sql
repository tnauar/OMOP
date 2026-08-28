CREATE TABLE omop.CSV_raw (
        row_id SERIAL PRIMARY KEY,
        visit_index INTEGER,
        visit_date DATE,
        visit_type TEXT,
        visit_id INTEGER,
        healthcare_plan TEXT,
        person_id INTEGER,
        gender CHAR,
        name TEXT,
        age INTEGER,
        condition TEXT,
        duration TEXT,
        symptom_1 TEXT,
        symptom_2 TEXT,
        medication TEXT,
        free_text TEXT
);
