import sqlite3

db = sqlite3.connect("workout_log.db")
cursor = db.cursor()

cursor.execute("""
    CREATE TABLE workouts(
        id INTEGER PRIMARY KEY,
        date TEXT NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE exercises(
        id INTEGER PRIMARY KEY,
        workout_id INTEGER NOT NULL REFERENCES workouts(id),
        name TEXT NOT NULL,
        weight INTEGER NOT NULL,
        reps INTEGER NOT NULL,
        sets INTEGER NOT NULL
    )  
""")

db.commit()
db.close()
