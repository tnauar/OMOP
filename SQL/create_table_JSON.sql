CREATE TABLE omop.JSON_raw (
        row_id SERIAL PRIMARY KEY,
        visit_index INTEGER,
        person_id INTEGER,
        gender CHAR,
        name TEXT,
        age INTEGER,
        visit_date DATE,
        visit_type TEXT,
        visit_id INTEGER,
        symptom_1 TEXT,
        symptom_2 TEXT,
        medication TEXT,
        condition TEXT,
        duration TEXT,
        free_text TEXT
);
