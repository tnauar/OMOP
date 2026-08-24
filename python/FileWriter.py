import pandas as pd
import pyarrow

class FileWriter():
    def __init__(self):
        pass

    def write(self, data, filetype):

        self.df = pd.DataFrame(data)

        if filetype == "csv":
            self.write_csv()
        elif filetype == "json":
            self.write_json()
        elif filetype == "xlsx":
            self.write_xlsx()
        elif filetype == "parquet":
            self.write_parquet()
        else:
            self.write_csv()
            

    def write_csv(self):
        self.df.to_csv("esimerkki.csv", index=False)

    def write_json(self):
        self.df.to_json("esimerkki.json", orient="records", force_ascii=False, indent=2)

    def write_xlsx(self):
        self.df.to_excel("esimerkki.xlsx", index=False)

    def write_parquet(self):
        self.df.to_parquet("esimerkki.parquet", index=False)