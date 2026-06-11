import psycopg2
from src import reader, clean, validate ,database
reading = reader.ReadData("ETL.log")
data = reading.read_csv("data\\raw\\gym_members_exercise_tracking.csv")
transfer = database.DatabaseOperations(data)

db = transfer.connect_to_database()
transfer.create_table(db)
transfer.insert_data(db)

print(data)