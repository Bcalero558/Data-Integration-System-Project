import pandas as pd

class Cleaner:
    
    data = pd.DataFrame()
    def __init__(self,df :pd.DataFrame):
        self.data= df.copy
        

    def clean(self) -> pd.DataFrame:
        unique = self.data.drop_duplicates()
        dupe = self.data[self.data.duplicated()]

        if len(dupe) > 0:
            dupe['reason'] = 'Duplicate' 
        dupe.to_csv('rejected.csv', index = False)
        return unique
    
        
