import random
import csv
import pandas
from datetime import date, timedelta
from RandomData import RandomData
from FileWriter import FileWriter

class DataCollector():

    def __init__(self):
        file_writer = FileWriter()

    """We will plant some error to the these three fields below."""

    def choose_symptoms(self):
        (sym1, sym2)= random.sample(RandomData.SYMPTOM_BANK, 2)
        planted_error = random.choices(["no", "yes"], k=1, weights=[0.99, 0.01])[0]
        if planted_error == "yes":
            return ("Err", sym2)
        return (sym1, sym2)

    def choose_medications(self):
        med1 = random.choice(RandomData.MEDICATIONS)
        planted_error = random.choices(["no", "yes"], k=1, weights=[0.99, 0.01])[0]
        if planted_error == "yes":
            return "null"
        return med1

    def choose_conditions(self):
        cond1 = random.choice(RandomData.CONDITIONS)
        planted_error = random.choices(["no", "yes"], k=1, weights=[0.99, 0.01])[0]
        if planted_error == "yes":
            return " "
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

    """These are extra random fields that bring diversity to the data."""
    def choose_nationality(self):
        nationality = random.choices(RandomData.NATIONALITY, weights=[0.88, 0.05, 0.02, 0.02, 0.01, 0.01, 0.01], k=1)[0]
        return nationality

    def choose_healthcare_plan(self):
        healthcare_plan = random.choices(RandomData.HEALTHCARE_PLAN, weights=[0.4, 0.15, 0.05, 0.4], k=1)[0]
        return healthcare_plan

    def choose_education(self):
        education = random.choices(RandomData.EDUCATION, weights=[0.2, 0.2, 0.4, 0.15, 0.05], k=1)[0]
        return education

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


    def collect_data(self, filetype):

        # Täällä siis tehtäisiin yksi iso dict, joka sitten tulostettaisiin tiedostoihin eri menetelmillä.
        # Ei tehtäisiin yksi dict tietylle tietotyypille ja sen omilla sarakkeilla random järjestyksessä.
        # Ei tehdä liian monimutkaista. Kirjoitan data dictiin ja saman kaikille.
        # Tässä se ero pitäisi tehdä tehdään if rakenteeseen useampi dictin muodostus sen mukaan
        # mikä tiedostotyyppi on kyseessä. Sillä tavalla ainakin saisi niihin eroa, mutta silloin tulisi
        # jonkin verran koodin toistoa.



        visit_index = 20000 + random.randint(4000, 9000)
        START_DATE = date(2025, 1, 1)

        rows = []

        for i in range(1, 500):

            visit_index = visit_index + i
            person_id = 10000 + random.randint(1, 5000)
            gender = random.choices(["N", "M", "T"], weights=[0.5, 0.48, 0.2])
            firstname, lastname = self.choose_name(gender)
            patient_name = f"{firstname} {lastname}"
            age = random.randint(1, 100)
            visit_date = START_DATE + timedelta(days=random.randint(0, 365))
            visit_type, visit_id = random.choice(RandomData.VISIT_TYPES)
            (sym_1, sym_2) = self.choose_symptoms()
            medication = self.choose_medications()
            condition = self.choose_conditions()
            duration = self.choose_durations()
            vacc_keyword = self.choose_vacc_keyword()
            vacc_place = self.choose_vacc_place()
            vacc_type = self.choose_vacc_type()
            type = random.choices(["normal", "vacc"], weights=[0.8, 0.2])
            nationality = self.choose_nationality()
            healthcare_plan = self.choose_healthcare_plan()
            education = self.choose_education()
            free_text = self.free_text_gen(sym_1, sym_2, medication, condition, duration, vacc_keyword, vacc_place, vacc_type, type)

            if filetype == "json":
                row = {
                    "rivi_nro": i,
                    "käynti_id": visit_index,
                    "henkilö_id": person_id,
                    "sukupuoli": gender[0],
                    "potilaan_nimi": patient_name,
                    "ikä": age,
                    "käynnin_päivämäärä": visit_date.isoformat(),
                    "käynnin_tyyppi": visit_type,
                    "käynnin_id": visit_id,
                    "oire_1": sym_1,
                    "oire_2": sym_2,
                    "lääkitys": medication,
                    "tila": condition,
                    "kesto": duration,
                    "vapaa_teksti": free_text
                }
                rows.append(row)
            elif filetype == "parquet":
                row = {
                    "rivi_nro": i,
                    "käynti_id": visit_index,
                    "henkilö_id": person_id,
                    "kansallisuus": nationality,
                    "koulutus": education,
                    "sukupuoli": gender[0],
                    "potilaan_nimi": patient_name,
                    "ikä": age,
                    "käynnin_päivämäärä": visit_date.isoformat(),
                    "käynnin_tyyppi": visit_type,
                    "käynnin_id": visit_id,
                    "tila": condition,
                    "kesto": duration,
                    "oire_1": sym_1,
                    "oire_2": sym_2,
                    "lääkitys": medication,
                    "mitä_kautta": healthcare_plan,
                    "vapaa_teksti": free_text
                }
                rows.append(row)                
            elif filetype == "xlsx":
                row = {
                    "rivi_nro": i,
                    "käynti_id": visit_index,
                    "henkilö_id": person_id,
                    "kansallisuus": nationality,
                    "koulutus": education,
                    "potilaan_nimi": patient_name,
                    "sukupuoli": gender[0],
                    "ikä": age,
                    "käynnin_päivämäärä": visit_date.isoformat(),
                    "käynnin_tyyppi": visit_type,
                    "käynnin_id": visit_id,
                    "tila": condition,
                    "kesto": duration,
                    "oire_1": sym_1,
                    "oire_2": sym_2,
                    "lääkitys": medication,
                    "vapaa_teksti": free_text
                } 
                rows.append(row)
            else:
                row = {
                    "rivi_nro": i,
                    "käynti_id": visit_index,
                    "käynnin_päivämäärä": visit_date.isoformat(),
                    "käynnin_tyyppi": visit_type,
                    "käynnin_id": visit_id,
                    "mitä_kautta": healthcare_plan,
                    "henkilö_id": person_id,
                    "sukupuoli": gender[0],
                    "potilaan_nimi": patient_name,
                    "ikä": age,
                    "tila": condition,
                    "kesto": duration,
                    "oire_1": sym_1,
                    "oire_2": sym_2,
                    "lääkitys": medication,
                    "vapaa_teksti": free_text
                }
                rows.append(row)       
        return rows

