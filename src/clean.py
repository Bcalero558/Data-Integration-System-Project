import pandas as pd

class Cleaner:
    
    data = pd.DataFrame()
    def __init__(self,df :pd.DataFrame):
        self.data= df.copy
        
    # cleans and formats data for proper use
    def clean_row(self) :
        pass
    
    def clean_rows(self):
        pass

        
