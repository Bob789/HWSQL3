import sqlite3

try:
    # Connect to the database
    db_name = "HWSQL3.05.01.25.db"
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row  # Access by column name

    # Create a cursor
    cursor = conn.cursor()

    # Select rows to UPDATE
    cursor.execute("SELECT * FROM shopping WHERE name LIKE 'Milk' AND amount != 1")
    rows_to_update = cursor.fetchall()

    # Display the rows that will be update
    if rows_to_update:
        print("The following rows will be UPDATE:")
        for row in rows_to_update:
            print(dict(row))
        # Confirm update
        print("Row update successfully!")
    else:
        print("No rows matched the condition.")

    # Update the selected rows
    cursor.execute("UPDATE shopping SET amount=1 WHERE name LIKE 'Milk'")

    # Commit the changes
    conn.commit()

except sqlite3.Error as e:
    # Print error message if something goes wrong
    print(f"An error occurred: {e}")

finally:
    # Close the connection
    if conn:
        conn.close()
