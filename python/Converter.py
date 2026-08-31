import pandas as pd

class Converter:

    def main(self):
        """Reads an excel, json and parquet file from disk and converts it to csv file using pandas.
        
        Args:
            None.
            
        Returns: None.
        """

        df_excel = pd.read_excel("./random_data/random_data_3.xlsx")
        df_json = pd.read_json("./random_data/random_data_2.json")
        df_parquet = pd.read_parquet("./random_data/random_data_4.parquet")

        df_excel.to_csv("./random_data/random_data_excel.csv", index=False)
        df_json.to_csv("./random_data/random_data_json.csv", index=False)
        df_parquet.to_csv("./random_data/random_data_parquet.csv", index=False)

if __name__ == "__main__":
    Converter().main()