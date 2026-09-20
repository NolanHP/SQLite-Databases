import sqlite3

def create_tables(db):
    cursor = db.cursor()    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS workouts(
            id INTEGER PRIMARY KEY,
            date TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS exercises(
            id INTEGER PRIMARY KEY,
            workout_id INTEGER NOT NULL REFERENCES workouts(id),
            name TEXT NOT NULL,
            weight INTEGER NOT NULL,
            reps INTEGER NOT NULL,
            sets INTEGER NOT NULL
        )  
    """)
    
db = sqlite3.connect("workout_log.db")
create_tables(db)
db.commit()
db.close()
