import sqlite3
from datetime import datetime

def get_valid_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Try again.")
    

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


cont_add = "y"
while cont_add == "y":
    exercise_name = input("Please enter the name of the exercise: ")
    weight = get_valid_int("Enter weight: ")
    reps = get_valid_int("Enter # of reps: ")
    sets = get_valid_int("Enter # of sets: ")
        
    cursor.execute("INSERT INTO exercises (workout_id, name, weight, reps, sets) VALUES(?, ?, ?, ?, ?)", (new_workout_id, exercise_name, weight, reps, sets,))
    cont_add = input("Add an exercise(y/n): ")

db.commit()