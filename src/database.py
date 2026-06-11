import psycopg2
import pandas as pd
from sqlalchemy import create_engine

class DatabaseOperations:
    data = pd.DataFrame()
    
    #takes in pandas dataframe for insertion
    def __init__(self, data):
        self.data = data

    #connect to postgres
    #todo:
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
            bmi DECIMAL(4,2)
            )

        """
        )
        conn.commit()
        print("Created Table Successfully")
        
    #add elements to table
    def insert_data(self,conn):
        data_list = self.data.list()
        query = """
        INSERT INTO members (
        age,gender,weight,height,max_bpm,avg_bpm,resting_bpm,session_duration,
        calories_burned,workout_type,fat_percentage,water_intake,Workout_Frequency,
        experience_level,bmi) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """

        with conn.cursor() as cursor:
            cursor.executemany(
                query,
                [
                    (
                        row["Age"],
                        row["Gender"],
                        row["Weight (kg)"],
                        row["Height (m)"],
                        row["Max_BPM"],
                        row["Avg_BPM"],
                        row["Resting_BPM"],
                        row["Session_Duration (hours)"],
                        row["Calories_Burned"],
                        row["Workout_Type"],
                        row["Fat_Percentage"],
                        row["Water_Intake (liters)"],
                        row["Workout_Frequency (days/week)"],
                        row["Experience_Level"],
                        row["BMI"]
                    )
                    for row in data_list
                ],
            )
        conn.commit()

