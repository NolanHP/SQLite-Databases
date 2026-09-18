import sqlite3
from datetime import datetime

db = sqlite3.connect("workout_log.db")
cursor = db.cursor()

while True:
    user_date = input("Enter date (YYYY-MM-DD): ")
    try:
        datetime.strptime(user_date, "%Y-%m-%d")
        break
    except ValueError:
        print("Invalid date format, try again.")

cursor.execute("INSERT INTO workouts (date) VALUES (?)", (user_date,))
new_workout_id = cursor.lastrowid
db.commit()