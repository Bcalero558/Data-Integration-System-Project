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

    #Create table
    def create_table(conn):
        cursor = conn.cursor()
        cursor.execute(
        """
            CREATE TABLE IF NOT EXIST members(
            id SERIAL PRIMARY KEY,
            age INT NOT NULL
            gender VARCHAR(6)
            weight DECIMAL(4,1),
            height DECIMAL(3,2),
            max_bpm INT NOT NULL
            avg_bpm INT NOT NULL
            resting_bpm INT NOT NULL
            session_duration DECIMAL(3,2)
            calories_burned DECIMAL(5,1)
            workout_type VARCHAR(255)
            fat_percentage DECIMAL(3,1)
            water_intake DECIMAL(2,1)
            Workout_Frequency INT NOT NULL
            experience_level INT NOT NULL
            BMI DECIMAL(4,2)
            )

        """
        )
        conn.commit()
        print("Created Table Successfully")
    

