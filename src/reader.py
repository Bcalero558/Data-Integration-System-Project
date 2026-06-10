import pandas as pd
import json
import requests
import logging

class ReadData:
    logger = None
    def __init__(self,log_file):
        self.csv_data = None
        self.json_data=None
        self.api_data=None
        self.logger = logging.get_logger(log_file)
    
    
    logger.setLevel(logging.DEBUG)



    def read_csv(self,filename):
        try:
            csv_data = pd.read_csv(filename)
        except Exception as e:
            self.logger.Error("Error: Reading CSV File")
        else:
            return csv_data
    