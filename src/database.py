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
            logging.error(f"Failed to Connect {username}, {host}, {database}")


    def config_setup(self,config):
        if config:
            """example of what to put in the terminal to make the file to function

                $env:POSTGRES_HOST = 'localhost'
                $env:POSTGRES_PORT = '5432'
                $env:POSTGRES_DB = 'ETL_pipeline_project'
                $env:POSTGRES_USER = 'postgres'
                $env:POSTGRES_PASSWORD = 'postgres'
            """
            # Extract the environment variables
            postgres_user = os.environ.get('POSTGRES_USER', 'default_value')
            postgres_password = os.environ.get('POSTGRES_PASSWORD', 'default_value')
            postgres_db = os.environ.get('POSTGRES_DB', 'default_value')
            

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
            logging.info(f'Postgres Info = Host: {host}, Username: {username}, Database: {database}')

                 # Establish a connection to the PostgreSQL database
            return self.connect_to_database(host,port,username,password,database)
        else:
            logging.error("Failed to load configuration.")


#creates table with modular name and columns
    def create_table(self,conn,table_name,*columns):
        try:
            cursor = conn.cursor()
            columns_str = ','.join(columns)
            query = f"""
                    CREATE TABLE IF NOT EXISTS {table_name}(
                    {columns_str}
                    );  
                """
            cursor.execute(query)
            conn.commit()
            logging.info("Created Table Successfully")
        except:
            logging.error("Table Not Created")
            

    #add elements to table
    def insert_data(self,conn,data,table_name):
        try:
            self.table_insert_params(data,conn,table_name)
            logging.info("Data Inserted")
        except:
            logging.error("Failed to Insert Data")
    



    #basic select function
    def query_all(self,conn, table_name):
        try:
            query = f"SELECT * FROM {table_name} LIMIT 10"
            result =  pd.read_sql(query, conn)
        except:
            logging.error("Data Not Found")
        else:
            logging.info("Data Read")
            return result



    #Changes Parameters depending on table
    def table_insert_params(self,data,conn,table_name):
          #makes the values from data into a list
            data_list = data.to_records(index = False)
            #makes a placeholder string for SQL Code
            if(table_name == "members"):
                query = f"""

                INSERT INTO {table_name} (
                age,gender,weight,height,max_bpm,avg_bpm,resting_bpm,session_duration,
                calories_burned,workout_type,fat_percentage,water_intake,Workout_Frequency,
                experience_level,bmi) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                """
            
            #Executes the query string in SQL replacing values with what is given
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
                            #continues while there are rows of data
                            for row in data_list
                    ],
                )
            elif(table_name == "exercises"):
                query = f"""
                        INSERT INTO {table_name}(exercise_name,exercise_type,description,muscle_group,equipment_needed)
                        VALUES (%s,%s,%s,%s,%s)
                        """
                with conn.cursor() as cursor:
                    cursor.executemany(
                        query,
                        [
                            (
                                 row["exercise_name"],
                                 row["exercise_type"],
                                 row["description"],
                                 row["muscle_group"],
                                 row["equipment_needed"]
                                 
                            )
                            #continues while there are rows of data
                            for row in data_list
                    ],
                )
            conn.commit()

