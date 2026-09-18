import sqlite3


db = sqlite3.connect("workout_log.db")
cursor = db.cursor()

cursor.execute("SELECT id, date FROM workouts")
rows = cursor.fetchall()


for row in rows:
    print(str(row[0])+ ": " +row[1])
    
while True:
    try:    
        user_selected_id = int(input("Please select a #: "))
        cursor.execute("SELECT workouts.date, exercises.name, exercises.weight, exercises.reps, exercises.sets FROM workouts JOIN exercises ON workouts.id = exercises.workout_id WHERE workouts.id = (?)",(user_selected_id,))
        rows = cursor.fetchall()
        if rows:
            for row in rows:
                print("Date: " + row[0] + ", Exercise: "+ row[1]+ ", Weight: " + str(row[2])+ ", Reps: " + str(row[3])+ ", Sets: " + str(row[4]))
            break 
        print("Invalid input. Try again")
    except ValueError:
        print("Invalid input. Try again")
    


    