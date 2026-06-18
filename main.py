import psycopg2
from src import reader, validate ,database
import logging

#TODO : add logging, add Config file, Make SQL Calls more modular, Add UI,
#add second table to be referenced

logging.basicConfig(
 level=logging.DEBUG,  # sets the root logging level 
 filename='ETL.log',  # tells the root logger where to save the log file (relative path)
 filemode='a',  # tells the root logger to append the logs (not save over)
 format='%(name)s - %(levelname)s - %(message)s'  # tells the root logger how to format the logs
)
def main():
    #a list to store the format of the csv file 
    gm_format_str = ["Age","Gender","Weight (kg)","Height (m)","Max_BPM","Avg_BPM","Resting_BPM","Session_Duration (hours)","Calories_Burned","Workout_Type","Fat_Percentage","Water_Intake (liters)","Workout_Frequency (days/week)","Experience_Level","BMI"]
    #name of the file
    gm_file_name = "data\\raw\\gym_members_exercise_tracking.csv"
    gm_reading = reader.ReadData('ETL.log')
    gm_data = gm_reading.read_csv(gm_file_name,gm_format_str)
    #a list of conditionals saved as a string in order to use in the validator to save reason of rejection
    gm_conditions = ["data[\"Age\"] < 100" , "data[\"Max_BPM\"] < 220" , "data[\"Resting_BPM\"] > 30"]
    gm_validator = validate.Validator(gm_data)

    gm_validator.validate_rows(gm_conditions,gm_data)
    gm_data = gm_reading.read_csv("data\\processed\\clean_data.csv",gm_format_str)

    gm_transfer = database.DatabaseOperations('ETL.log')
    gm_db = gm_transfer.connect_to_database()
    gm_transfer.create_table(gm_db)
    gm_transfer.insert_data(gm_db,gm_data)

    query = gm_transfer.query(gm_db)


    print(query)
if __name__ == "__main__":
    main()