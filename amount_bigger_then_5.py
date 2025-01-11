import sqlite3

try:
    # Create a new database
    db_name = "HWSQL3.05.01.25.db"
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row  # Access by column name

    # Create a cursor
    cursor = conn.cursor()

    #################### read from db
    cursor.execute("SELECT * FROM shopping WHERE amount > 5")
    rows = cursor.fetchall()
    result_list = [list(row) for row in rows]

    for result in result_list:
        print(result)

    print("Data Rows are fetchall successfully!")

except sqlite3.Error as e:
    # Print error message if something goes wrong
    print(f"An error occurred: {e}")

finally:
    # Close the connection
    if conn:
        conn.close()
