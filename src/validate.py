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

        #determines if there are any duplicates in the data
        duplicates = data.duplicated()

        #accepts data without duplicates and saves data with duplicates
        accepted_row = data.drop_duplicates( keep ='first')
        rejected_row = data[duplicates].assign(Error = "Duplicate")
        


        #checks through given conditions to reject and accept rows
        for i in condition:
            rejected_row = pd.concat([rejected_row,accepted_row[~eval(i)]])
            accepted_row = accepted_row[eval(i)]
        
        #saves processed data
        accepted_row.to_csv('data\\processed\\clean_data.csv')
        rejected_row.to_csv('data\\processed\\rejected_data.csv')
