import psycopg2
from psycopg2.extras import RealDictCursor
import pandas as pd
import logging
import json 
import os

class DatabaseOperations:
    data = pd.DataFrame()
    
    #takes in pandas dataframe for insertion
    def __init__(self, log_file):
        self.logger = logging.getLogger(log_file)
        self.logger.setLevel(logging.DEBUG)


    








    #connect to postgres
    def connect_to_database(self,host,port,username,password,database):
        try:
            conn = psycopg2.connect(
                dbname = database,
                user = username,
                password = password,
                host = host,
                port = port
                )
            logging.info(f"Connecting to PostgreSQL server:{host}:{port} as User {username}")
            return conn
        except Exception as e:
            logging.error(f"Failed to Connect {password}, {username}, {host}, {port}, {database}")

    def config_setup(self,config):
        if config:
            # Extract the environment variables
            postgres_user = os.environ.get('POSTGRES_USER', 'postgres')
            postgres_password = os.environ.get('POSTGRES_PASSWORD', 'password')
            postgres_db = os.environ.get('POSTGRES_DB', 'ETL_pipeline_project')
            

    # Update the configuration with environment variables
            config['connection']['username'] = postgres_user
            config['connection']['password'] = postgres_password
            config['database'] = postgres_db

            host = config['connection']['host']
            port = config['connection']['port']
            username = config['connection']['username']
            password = config['connection']['password']
            database = config['database']

             # Print the configuration settings
            logging.info(f'Postgres Info = Host: {host}, Port: {port}, Username: {username}, Password: {password}, Database: {database}')

                 # Establish a connection to the PostgreSQL database
            return self.connect_to_database(host,port,username,password,database)
        else:
            logging.error("Failed to load configuration.")



    #Create table
    def create_table(self,conn):
        try:
            cursor = conn.cursor()
            cursor.execute(
            """
                DROP TABLE IF EXISTS members;
                CREATE TABLE IF NOT EXISTS members(
                id SERIAL PRIMARY KEY,
                age INT NOT NULL,
                gender VARCHAR(6),
                weight DECIMAL(4,1),
                height DECIMAL(3,2),
                max_bpm INT NOT NULL,
                avg_bpm INT NOT NULL,
                resting_bpm INT NOT NULL,
                session_duration DECIMAL(3,2),
                calories_burned DECIMAL(5,1),
                workout_type VARCHAR(255),
                fat_percentage DECIMAL(3,1),
                water_intake DECIMAL(2,1),
                Workout_Frequency INT NOT NULL,
                experience_level INT NOT NULL,
                bmi DECIMAL(4,2)
                )
            """
            )
            conn.commit()
            logging.info("Created Table Successfully")
        except:
            logging.error("Table Not Created")
            

    #add elements to table
    def insert_data(self,conn,data):
        try:
            data_list = data.to_records(index = False)
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
                            int(row["Age"]),
                            row["Gender"],
                            float(row["Weight (kg)"]),
                            float(row["Height (m)"]),
                            int(row["Max_BPM"]),
                            int(row["Avg_BPM"]),
                            int(row["Resting_BPM"]),
                            float(row["Session_Duration (hours)"]),
                            float(row["Calories_Burned"]),
                            row["Workout_Type"],
                            float(row["Fat_Percentage"]),
                            float(row["Water_Intake (liters)"]),
                            int(row["Workout_Frequency (days/week)"]),
                            int(row["Experience_Level"]),
                            float(row["BMI"])
                        )
                        for row in data_list
                    ],
                )
            conn.commit()
            logging.info("Data Inserted")
        except:
            logging.error("Failed to Insert Data")

    def query(self,conn):
        try:
            query = "SELECT * FROM members"
            result =  pd.read_sql(query, conn)
        except:
            logging.error("Data Not Found")
        else:
            logging.info("Data Read")
            return result

