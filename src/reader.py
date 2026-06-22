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

    
    


    # reads csv files, accepts a file name and column list
    def read_csv(self,filename,format_list):
        try:
            csv_data = pd.read_csv(filename)
            final = csv_data[format_list]
        except Exception as e:
            #tells you which file was read
            logging.error(f"Issue With Reading CSV File at {filename}")
        else:
            logging.info(f"CSV File at {filename} Read Successfully")
            return final

    #reads data from JSON file
    def load_config(self,config_file_path):
        try:
            with open(config_file_path, 'r') as file:
                config_data = file.read()
                config_dict = json.loads(config_data)



        except FileNotFoundError:
            logging.error(f"Config File Not Found at {config_file_path}")
            return None
        except json.JSONDecodeError as e:
            logging.error(f"JSON Reading Error at {config_file_path}")
            return None
        else:
            logging.info(f"Config File {config_file_path} Read Successfully")
            return config_dict



           

    