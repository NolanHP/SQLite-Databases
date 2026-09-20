import sqlite3
from log_workout import insert_workout, insert_exercise
from init_db import create_tables

db = sqlite3.connect(":memory:")
cursor = db.cursor()

create_tables(db)

def test_insert_workout():
    result = insert_workout(db, "2008-03-04")
    assert result == 1
