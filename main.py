import psycopg2
from src import reader, clean, validate ,database
#a list to store the format of the csv file 
format_str = ["Age","Gender","Weight (kg)","Height (m)","Max_BPM","Avg_BPM","Resting_BPM","Session_Duration (hours)","Calories_Burned","Workout_Type","Fat_Percentage","Water_Intake (liters)","Workout_Frequency (days/week)","Experience_Level","BMI"]
#name of the file
file_name = "data\\raw\\gym_members_exercise_tracking.csv"
reading = reader.ReadData("ETL.log")
data = reading.read_csv(file_name,format_str)
#a list of conditionals saved as a string in order to use in the validator to save reason of rejection
conditions = ["data[\"Age\"] < 100" , "data[\"Max_BPM\"] < 220" , "data[\"Resting_BPM\"] > 30"]
validator = validate.Validator(data)

validator.validate_rows(conditions,data)
data = reading.read_csv("data\\processed\\clean_data.csv",format_str)

transfer = database.DatabaseOperations(data)
db = transfer.connect_to_database()
transfer.create_table(db)
transfer.insert_data(db)

print(data)