import sqlite3
import os
try:
    # Define the database name
    # db_name = "hw_solution.db"
    db_name = "hw_solution.db"

    # Check if the database file exists
    if os.path.exists(db_name):
        os.remove(db_name)
        print(f"Database '{db_name}' deleted.")
    else:
        print(f"Database '{db_name}' does not exist.")

except os.Error as e:
    # Print error message if something goes wrong
    print(f"An error occurred: {e}")

