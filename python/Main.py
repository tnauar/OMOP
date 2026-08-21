import random
import csv
from datetime import date, timedelta
from RandomData import RandomData

class Main:

    def main(self):

        self.write_file()

    def choose_symptoms(self):
        (sym1, sym2)= random.sample(RandomData.SYMPTOM_BANK, 2)
        return (sym1, sym2)

    def choose_medications(self):
        med1 = random.choice(RandomData.MEDICATIONS)
        return med1

    def choose_conditions(self):
        cond1 = random.choice(RandomData.CONDITIONS)
        return cond1

    def choose_durations(self):
        dur1 = random.choice(RandomData.DURATIONS)
        return dur1

    def choose_templates(self):
        temp1 = random.choice(RandomData.TEMPLATES)
        return temp1

    def choose_name(self, gender):

        if gender[0] == "T":
            gender = random.choice(["M", "N"]) 

        if gender[0] == "M":
            firstname = random.choice(RandomData.FIRST_NAMES_MALE)
            lastname = random.choice(RandomData.LAST_NAMES)
            return firstname, lastname
        else:
            firstname = random.choice(RandomData.FIRST_NAMES_FEMALE)
            lastname = random.choice(RandomData.LAST_NAMES)
            return firstname, lastname

    def choose_vacc_keyword(self):
        return random.choice(RandomData.VACCINATION_KEYWORD)

    def choose_vacc_place(self):
        return random.choice(RandomData.VACCINATION_PLACE)

    def choose_vacc_type(self):
        return random.choice(RandomData.VACCINATION_TYPE)

    def free_text_gen(self, sym_1, sym_2, medication, condition, duration, vacc_keyword, vacc_place, vacc_type, type):

        if type[0] == "normal":
            template = random.choice(RandomData.TEMPLATES)
            return template.format(
            sym1=sym_1,
            sym2=sym_2,
            med1=medication,
            duration=duration,
            condition=condition
        )
        else:
            template = random.choice(RandomData.TEMPLATES_VACC)
            return template.format(
            vacc_keyword=vacc_keyword,
            vacc_place=vacc_place,
            vacc_type=vacc_type
        )


    def write_file(self):

        try:
            with open("omop_visit_exercise_fi.csv", "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow([
                    "rivi",
                    "käynti_id",
                    "henkilö_id",
                    "sukupuoli",
                    "potilaan_nimi",
                    "ikä",
                    "käyntipäivä",
                    "käynnin_tyyppi",
                    "oire_1",
                    "oire_2",
                    "lääke",
                    "potilaan_tila",
                    "oireiden kesto",
                    "vapaa_teksti"
                ])


                visit_id = 20000 + random.randint(4000, 9000)
                START_DATE = date(2025, 1, 1)

                for i in range(1, 10):

                    visit_id = visit_id + i
                    person_id = 10000 + random.randint(1, 5000)
                    gender = random.choices(["N", "M", "T"], weights=[0.5, 0.48, 0.2])
                    firstname, lastname = self.choose_name(gender)
                    patient_name = f"{firstname} {lastname}"
                    age = random.randint(1, 100)
                    visit_date = START_DATE + timedelta(days=random.randint(0, 365))
                    visit_type = random.choice(RandomData.VISIT_TYPES)
                    (sym_1, sym_2) = self.choose_symptoms()
                    medication = self.choose_medications()
                    condition = self.choose_conditions()
                    duration = self.choose_durations()
                    vacc_keyword = self.choose_vacc_keyword()
                    vacc_place = self.choose_vacc_place()
                    vacc_type = self.choose_vacc_type()
                    type = random.choices(["normal", "vacc"], weights=[0.8, 0.2])
                    free_text = self.free_text_gen(sym_1, sym_2, medication, condition, duration, vacc_keyword, vacc_place, vacc_type, type)

                    writer.writerow([
                    i,
                    visit_id,
                    person_id,
                    gender[0],
                    patient_name,
                    age,
                    visit_date.isoformat(),
                    visit_type,
                    sym_1,
                    sym_2,
                    medication,
                    condition,
                    duration,
                    free_text
                    ])

        except PermissionError as e:
            return e, "error"        

if __name__ == "__main__":
    Main().main()