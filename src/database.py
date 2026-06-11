import psycopg2
import pandas as pd
from sqlalchemy import create_engine

class DatabaseOperations:
    data = pd.DataFrame()
    
    #takes in pandas dataframe for insertion
    def __init__(self, data):
        self.data = data

    def connect_to_database():
        try:
            conn = psycopg2.connect(
                dbname = "ETL_pipeline_project",
                user = "postgres",
                password = "password",
                host = "localhost",
                port = "5432"
                )
            print("Successful Connection")
            return conn
        except Exception as e:
            print("Failed to Connect")

    

