import psycopg2
from src import reader, validate ,database
import logging
import sys
#TODO :  Make SQL Calls more modular, Add UI,add second table to be referenced

logging.basicConfig(
 level=logging.DEBUG,  # sets the root logging level 
 filename='ETL.log',  # tells the root logger where to save the log file (relative path)
 filemode='a',  # tells the root logger to append the logs (not save over)
 format='%(filename)s - %(levelname)s - %(message)s'  # tells the root logger how to format the logs
)

def main():


    #a list to store the format of the csv file columns
    gm_format_str = ["Age","Gender","Weight (kg)","Height (m)","Max_BPM","Avg_BPM","Resting_BPM","Session_Duration (hours)","Calories_Burned","Workout_Type","Fat_Percentage","Water_Intake (liters)","Workout_Frequency (days/week)","Experience_Level","BMI"]
    gm_table_name = "members"
    el_format_str = ["exercise_name","exercise_type","description","muscle_group","equipment_needed"]
    el_table_name = "exercises"
    #name  and path of the file
    gm_file_name = "data\\raw\\gym_members_exercise_tracking.csv"
    el_file_name = "data\\raw\\Exercise_List.csv"
    #creates an object for reading files
    reading = reader.ReadData('ETL.log')

    #config file path and save json config as dictionary
    config_file_path = 'src\postgres_config.json'
    config  = reading.load_config(config_file_path)

 
    #read csv data
    gm_data = reading.read_csv(gm_file_name,gm_format_str)
    el_data = reading.read_csv(el_file_name,el_format_str)
    #a list of conditionals saved as a string in order to use in the validator to save reason of rejection
    gm_conditions = ["data[\"Age\"] < 100" , "data[\"Max_BPM\"] < 220" , "data[\"Resting_BPM\"] > 30","data[\"Resting_BPM\"] < data[\"Max_BPM\"]", "data[\"Water_Intake (liters)\"] < 10.0" ,"data[\"Fat_Percentage\"] < 50.0"]
    #validate data to remove duplicates and logical error and changes data to cleaned csv
    gm_validator = validate.Validator(gm_data)
    gm_validator.validate_rows("data\\processed\\clean_data.csv",gm_data,gm_conditions)
    gm_validator.validate_rows("data\\processed\\clean_exercises.csv",el_data)
    gm_data = reading.read_csv("data\\processed\\clean_data.csv",gm_format_str)
    el_data = reading.read_csv("data\\processed\\clean_exercises.csv",gm_format_str)


    #enables database Operations
    gm_transfer = database.DatabaseOperations('ETL.log')
    #configures and connects to database
    gm_db = gm_transfer.config_setup(config)
    #creates table and stores data to postgres
    gm_transfer.create_table(gm_db,gm_table_name, 
                'member_id SERIAL PRIMARY KEY', 
                'age INT NOT NULL',
                'gender VARCHAR(6)',
                'weight DECIMAL(4,1)',
                'height DECIMAL(3,2)',
                'max_bpm INT NOT NULL',
                'avg_bpm INT NOT NULL',
                'resting_bpm INT NOT NULL',
                'session_duration DECIMAL(3,2)',
                'calories_burned DECIMAL(5,1)',
                'workout_type VARCHAR(255)',
                'fat_percentage DECIMAL(3,1)',
                'water_intake DECIMAL(2,1)',
                'Workout_Frequency INT NOT NULL',
                'experience_level INT NOT NULL',
                'bmi DECIMAL(4,2)'
    )
    gm_transfer.insert_data(gm_db,gm_data,gm_table_name)
    #creates second table
    gm_transfer.create_table(gm_db,el_table_name,
                            'exercise_id SERIAL PRIMARY KEY',
                            "exercise_name VARCHAR(255)",
                            "exercise_type VARCHAR(255)",
                            "description VARCHAR(255)",
                            "muscle_group VARCHAR(255)",
                            "equipment_needed VARCHAR(255)"
                            )
    gm_transfer.insert_data(gm_db,el_data,el_table_name)

    
    #checks if it can retrieve the data from postgres
    query = gm_transfer.query_all(gm_db,gm_table_name)
    logging.debug(query)
    query = gm_transfer.query_all(gm_db,el_table_name)
    logging.debug(query)
if __name__ == "__main__":
    main()