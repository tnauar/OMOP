import random
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

if __name__ == "__main__":
    Main().main()