import sqlite3
from log_workout import insert_workout, insert_exercise
from init_db import create_tables

db = sqlite3.connect(":memory:")
cursor = db.cursor()

create_tables(db)

def test_insert_workout():
    result = insert_workout(db, "2008-03-04")
    assert result == 1


def test_insert_exercise():
    workout_id_test = insert_workout(db, "2009-03-03")
    result = insert_exercise(db, workout_id_test, "Pushups", 100, 20, 3)
    cursor.execute("SELECT * FROM exercises WHERE id = (?);", (result,))
    row = cursor.fetchone()
    assert row == (result, workout_id_test, "Pushups", 100, 20, 3)