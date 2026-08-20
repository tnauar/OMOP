import random
import csv
from RandomData import RandomData

class Main:

    def main(self):
        print(RandomData.FIRST_NAMES)
        print(self.choose_symptoms())
        print(self.choose_medications())
        print(self.choose_conditions())
        print(self.choose_durations())
        print(self.choose_templates())

        (sym1, sym1_inflection), (sym2, sym2_inflection) = self.choose_symptoms()
        med1 = self.choose_medications()
        (cond1, cond1_inflection) = self.choose_conditions()
        dur1 = self.choose_durations()
        self.write_file()

        template = self.choose_templates()
        print(template.format(sym1=sym1_inflection, sym2=sym2_inflection, med1=med1, duration=dur1, condition=cond1))

    def choose_symptoms(self):
        (sym1, sym1_inflection), (sym2, sym2_inflection)= random.sample(RandomData.SYMPTOM_BANK, 2)
        return (sym1, sym1_inflection), (sym2, sym2_inflection)

    def choose_medications(self):
        med1 = random.choice(RandomData.MEDICATIONS)
        return med1

    def choose_conditions(self):
        (cond1, cond1_inflection) = random.choice(RandomData.CONDITIONS)
        return (cond1, cond1_inflection)

    def choose_durations(self):
        dur1 = random.choice(RandomData.DURATIONS)
        return dur1

    def choose_templates(self):
        temp1 = random.choice(RandomData.TEMPLATES)
        return temp1
        
    def write_file(self):

        try:
            with open("omop_visit_exercise_fi.csv", "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow([
                    "käynti_id",
                    "henkilö_id",
                    "potilaan_nimi",
                    "käyntipäivä",
                    "ikä",
                    "sukupuoli",
                    "käynnin_tyyppi",
                    "vapaa_teksti",
                    "oire_1",
                    "oire_2",
                    "lääke_1",
                    "lääke_2",
                    "potilaan_tila"
                ])
        except PermissionError:
            pass

    for i in range(1, 501):
        person_id = 10000 + random.randint(1, 5000)
        
        first = random.choice(FIRST_NAMES)
        last = random.choice(LAST_NAMES)
        patient_name = f"{first} {last}"

        visit_date = START_DATE + timedelta(days=random.randint(0, 365))
        age = random.randint(1, 95)
        sex = random.choice(["F", "M", "U"])

        visit_type, visit_concept_id = random.choice(VISIT_TYPES)
        chief_complaint, chief_complaint_fi = random.choice([
            ("Headache", "päänsärky"),
            ("Fever", "kuume"),
            ("Cough", "yskä"),
            ("Abdominal pain", "vatsakipu"),
            ("Dizziness", "huimaus"),
            ("Back pain", "selkäkipu"),
            ("Nausea", "pahoinvointi"),
            ("Shortness of breath", "hengenahdistus"),
        ])

        s1, s1_form, s2, s2_form, s3, s3_form = choose_symptoms()
        med1 = random.choice(MEDICATIONS)
        med2 = random.choice(MEDICATIONS + [""])

        condition_source, condition_acc = random.choice(CONDITIONS)
        condition_concept_id = random.randint(1000000, 9999999)
        drug_concept_id = random.randint(1000000, 9999999)

        duration = random.choice(DURATIONS)
        note = build_note(s1_form, s2_form, s3_form, med1, condition_acc, duration)

        mapping_hint = (
            "Map symptoms from note to condition/observation concepts; "
            "handle negation and uncertainty during NLP; map medication mentions to drug_exposure; "
            "preserve visit_type for visit_occurrence."
        )

        writer.writerow([
            i,
            person_id,
            patient_name,
            visit_date.isoformat(),
            age,
            sex,
            visit_type,
            visit_concept_id,
            chief_complaint_fi,
            note,
            s1,
            s2,
            s3,
            med1,
            med2 if med2 else "",
            condition_source,
            condition_concept_id,
            med1,
            drug_concept_id,
            mapping_hint
        ])        
        


if __name__ == "__main__":
    Main().main()