import pandas as pd

"""TODO:
    Removes invalid data and stores away elsewhere such as 
    Max_BPM < 220 
    resting bpm > 30
    age < 100
    Gender == Male || Female
    No duplicates
"""
class Validator:
    data = pd.DataFrame()
    def __init__(self,df):
        self.data= df.copy
        
    # TODO:cleans and formats data for proper use
    def validate_rows(self, condition,data) :

        accepted_row = data
        rejected_row = pd.DataFrame()
        for i in condition:
            rejected_row = rejected_row.append(accepted_row[~i], ignore_index = True)
            accepted_row = accepted_row[i]
        
        accepted_row.to_csv('data\\processed\\clean_data.csv')
        rejected_row.to_csv('data\\processed\\rejected_data.csv')
