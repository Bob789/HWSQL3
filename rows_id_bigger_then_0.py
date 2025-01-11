import sqlite3

try:
    # Connect to the database
    db_name = "HWSQL3.05.01.25.db"
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row  # Access by column name

    # Create a cursor
    cursor = conn.cursor()

    # Select rows WHERE id > 0
    cursor.execute("SELECT * FROM shopping WHERE id > 0")
    rows_id_bigger_then_0 = cursor.fetchall()

    if rows_id_bigger_then_0:
        # Display rows
        for row in rows_id_bigger_then_0:
            print(dict(row))
    else:
        print("No rows selected.")

except sqlite3.Error as e:
    # Print error message if something goes wrong
    print(f"An error occurred: {e}")

finally:
    # Close the connection
    if conn:
        conn.close()
