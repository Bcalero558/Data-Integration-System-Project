import pandas as pd
import json
import logging

class ReadData:
    logger = None
    
    #initial setup gets log file name from construction
    def __init__(self,log_file):
        self.csv_data = None
        self.json_data=None
        self.api_data=None
        self.logger = logging.getLogger(log_file)
        self.logger.setLevel(logging.DEBUG)

    
    


    # reads csv files
    def read_csv(self,filename):
        try:
            csv_data = pd.read_csv(filename)
        except Exception as e:
            self.logger.Error("Error: Reading CSV File")
        else:

            return csv_data[["Age","Gender","Weight (kg)","Height (m)","Max_BPM","Avg_BPM","Resting_BPM","Session_Duration (hours)","Calories_Burned","Workout_Type","Fat_Percentage","Water_Intake (liters)","Workout_Frequency (days/week)","Experience_Level","BMI"]]

    