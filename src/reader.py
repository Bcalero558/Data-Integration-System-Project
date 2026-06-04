import pandas as pd
import json
import requests

class ReadData:
    def __init__(self):
        self.csv_data = None
        self.json_data=None
        self.api_data=None
    
    def read_csv(self,filename):
        
    