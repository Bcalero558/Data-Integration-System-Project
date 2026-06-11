from src import reader, clean, validate 

reading = reader.ReadData("ETL.log")
data = reading.read_csv("data\\raw\\gym_members_exercise_tracking.csv")

print(data)