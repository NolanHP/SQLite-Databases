import sqlite3
from datetime import datetime

def insert_workout(db, date):
    cursor = db.cursor()
    try:
        datetime.strptime(date, "%Y-%m-%d")
        cursor.execute("INSERT INTO workouts (date) VALUES (?)", (date,))
    except ValueError:
        raise ValueError("Invalid date format: " + date)
    return cursor.lastrowid

def insert_exercise(db, workout_id, name, weight, reps, sets):
    cursor = db.cursor()
    cursor.execute("INSERT INTO exercises (workout_id, name, weight, reps, sets) VALUES(?, ?, ?, ?, ?)", (workout_id, name, weight, reps, sets,))
    return cursor.lastrowid


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
        workout_id = insert_workout(db, user_date)
        break
    except ValueError as e:
        print(e)
    
    

cont_add = "y"
while cont_add == "y":
    exercise_name = input("Please enter the name of the exercise: ")
    weight = get_valid_int("Enter weight: ")
    reps = get_valid_int("Enter # of reps: ")
    sets = get_valid_int("Enter # of sets: ")
        
    insert_exercise(db, workout_id, exercise_name, weight, reps, sets)
    cont_add = input("Add an exercise(y/n): ")

db.commit()