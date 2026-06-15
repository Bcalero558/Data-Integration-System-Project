import psycopg2
from src import reader, clean, validate ,database
format_str = ["Age","Gender","Weight (kg)","Height (m)","Max_BPM","Avg_BPM","Resting_BPM","Session_Duration (hours)","Calories_Burned","Workout_Type","Fat_Percentage","Water_Intake (liters)","Workout_Frequency (days/week)","Experience_Level","BMI"]
file_name = "data\\raw\\gym_members_exercise_tracking.csv"
reading = reader.ReadData("ETL.log")
data = reading.read_csv(file_name,format_str)
transfer = database.DatabaseOperations(data)

db = transfer.connect_to_database()
transfer.create_table(db)
transfer.insert_data(db)

print(data)