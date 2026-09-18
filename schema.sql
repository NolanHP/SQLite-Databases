CREATE TABLE workouts(
    id INTEGER PRIMARY KEY,
    date TEXT NOT NULL
);

CREATE TABLE exercises(
    id INTEGER PRIMARY KEY,
    workout_id INTEGER NOT NULL REFERENCES workouts(id),
    name TEXT NOT NULL,
    weight INTEGER NOT NULL,
    reps INTEGER NOT NULL,
    sets INTEGER NOT NULL
);