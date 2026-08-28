CREATE TABLE  omop.Excel_silver
AS
SELECT *,

CASE
    WHEN row_id IS NULL THEN FALSE
    WHEN visit_index IS NULL THEN FALSE
    WHEN visit_type IS NULL OR TRIM(visit_type) = '' OR TRIM(visit_type) = 'Err' OR TRIM(visit_type) = 'null' THEN FALSE
    WHEN visit_id IS NULL THEN FALSE
    WHEN person_id IS NULL THEN FALSE
    WHEN gender IS NULL OR TRIM(gender) = '' OR TRIM(gender) = 'Err' OR TRIM(gender) = 'null' THEN FALSE
    WHEN age IS NULL THEN FALSE
    WHEN symptom_1 IS NULL OR TRIM(symptom_1) = '' OR TRIM(symptom_1) = 'Err' OR TRIM(symptom_1) = 'null' THEN FALSE
    WHEN symptom_2 IS NULL OR TRIM(symptom_2) = '' OR TRIM(symptom_2) = 'Err' OR TRIM(symptom_2) = 'null' THEN FALSE
    WHEN medication IS NULL OR TRIM(medication) = '' OR TRIM(medication) = 'Err' OR TRIM(medication) = 'null' THEN FALSE
    WHEN condition IS NULL OR TRIM(condition) = '' OR TRIM(condition) = 'Err' OR TRIM(condition) = 'null' THEN FALSE
    WHEN duration IS NULL OR TRIM(duration) = '' OR TRIM(duration) = 'Err' OR TRIM(duration) = 'null' THEN FALSE
    WHEN free_text IS NULL OR TRIM(free_text) = '' OR TRIM(free_text) = 'Err' OR TRIM(free_text) = 'null' THEN FALSE
    WHEN firstname IS NULL OR TRIM(firstname) = '' OR TRIM(firstname) = 'Err' OR TRIM(firstname) = 'null' THEN FALSE
    WHEN lastname IS NULL OR TRIM(lastname) = '' OR TRIM(lastname) = 'Err' OR TRIM(lastname) = 'null' THEN FALSE

    ELSE TRUE
END                                                 AS is_valid,

CASE
    WHEN row_id IS NULL THEN 'Erroneous row_id'
    WHEN visit_index IS NULL THEN 'Erroneous visit_index'
    WHEN visit_type IS NULL OR TRIM(visit_type) = '' OR TRIM(visit_type) = 'Err' OR TRIM(visit_type) = 'null' THEN 'Erroneous visit_type'
    WHEN visit_id IS NULL THEN 'Erroneous visit_id'
    WHEN person_id IS NULL THEN 'Erroneous person_id'
    WHEN gender IS NULL OR TRIM(gender) = '' OR TRIM(gender) = 'Err' OR TRIM(gender) = 'null' THEN 'Erroneous gender'
    WHEN age IS NULL THEN 'Erroneous age'
    WHEN symptom_1 IS NULL OR TRIM(symptom_1) = '' OR TRIM(symptom_1) = 'Err' OR TRIM(symptom_1) = 'null' THEN 'Erroneous symptom_1'
    WHEN symptom_2 IS NULL OR TRIM(symptom_2) = '' OR TRIM(symptom_2) = 'Err' OR TRIM(symptom_2) = 'null' THEN 'Erroneous symptom_2'
    WHEN medication IS NULL OR TRIM(medication) = '' OR TRIM(medication) = 'Err' OR TRIM(medication) = 'null' THEN 'Erroneous medication'
    WHEN condition IS NULL OR TRIM(condition) = '' OR TRIM(condition) = 'Err' OR TRIM(condition) = 'null' THEN 'Erroneous condition'
    WHEN duration IS NULL OR TRIM(duration) = '' OR TRIM(duration) = 'Err' OR TRIM(duration) = 'null' THEN 'Erroneous duration'
    WHEN free_text IS NULL OR TRIM(free_text) = '' OR TRIM(free_text) = 'Err' OR TRIM(free_text) = 'null' THEN 'Erroneous free_text'
    WHEN firstname IS NULL OR TRIM(firstname) = '' OR TRIM(firstname) = 'Err' OR TRIM(firstname) = 'null' THEN 'Erroneous firstname'
    WHEN lastname IS NULL OR TRIM(lastname) = '' OR TRIM(lastname) = 'Err' OR TRIM(lastname) = 'null' THEN 'Erroneous lastname'
    
    ELSE NULL
END                                                 AS dq_error

FROM omop.Excel_bronze
