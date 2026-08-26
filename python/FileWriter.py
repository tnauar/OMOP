import pandas as pd

class FileWriter():

    def __init__(self):
        pass

    def write(self, data: list[dict], filetype: str) -> int:
        """Writes the random data to a file.
        
        Args:
            data: List of dicts that contain the data.
            filetype: A string that contains the type of the file. Values are csv, json, xlsx and parquet.
            
        Returns: 0 if everything went well. 1 if there was an exception.
        """

        self.df = pd.DataFrame(data)

        try:

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

        except Exception as e:
            print(f"Writing file failed because of {e}")
            return 1

        return 0

    def write_csv(self) -> None:
        self.df.to_csv("./random_data/random_data_1.csv", index=False)

    def write_json(self) -> None:
        self.df.to_json("./random_data/random_data_2.json", orient="records", force_ascii=False, indent=2)

    def write_xlsx(self) -> None:
        self.df.to_excel("./random_data/random_data_3.xlsx", index=False)

    def write_parquet(self) -> None:
        self.df.to_parquet("./random_data/random_data_4.parquet", index=False)