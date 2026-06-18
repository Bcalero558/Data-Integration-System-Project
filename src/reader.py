import pandas as pd
import json
import logging

class ReadData:
    
    
    #initial setup gets log file name from construction
    def __init__(self,log_file):
        self.csv_data = None
        self.json_data=None
        self.api_data=None
        self.logger = logging.getLogger(log_file)
        self.logger.setLevel(logging.DEBUG)

    
    


    # reads csv files
    def read_csv(self,filename,format_list):
        try:
            csv_data = pd.read_csv(filename)
            final = csv_data[format_list]
        except Exception as e:
            logging.error("Issue With Reading CSV File")
        else:
            logging.info("CSV File Read Successfully")
            return final


           

    