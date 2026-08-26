from DataCollector import DataCollector
from FileWriter import FileWriter

class Main:

    def main(self) -> None:
        """ This is the main class that controls the random file generation.
        For every file type (json, csv, parquet, xlsx) a random data is created in using DataCollector.
        For every file type the data columns are a bit different and some of the data fields 
        contain random errors.
        After data creation the data is written from the memory to the disk.
        The main point is that the data files content is different so that we can use SQL to set them in a same format. 
        """

        data_collector = DataCollector()
        file_writer = FileWriter()

        data = data_collector.collect_data("json")
        file_writer.write(data, "json")
    
        data = data_collector.collect_data("csv")
        file_writer.write(data, "csv")
    
        data = data_collector.collect_data("parquet")
        file_writer.write(data, "parquet")
    
        data = data_collector.collect_data("xlsx")
        file_writer.write(data, "xlsx")

if __name__ == "__main__":
    Main().main()