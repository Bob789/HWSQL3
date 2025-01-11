import sqlite3

try:
    # Connect to the database
    db_name = "HWSQL3.05.01.25.db"
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row  # Access by column name

    # Create a cursor
    cursor = conn.cursor()

    # Select rows to be deleted
    cursor.execute("SELECT * FROM shopping WHERE name LIKE 'Orange'")
    rows_to_delete = cursor.fetchall()

    # Display the rows that will be deleted
    if rows_to_delete:
        print("The following rows will be deleted:")
        for row in rows_to_delete:
            print(dict(row))

        # Delete the selected rows
        cursor.execute("DELETE FROM shopping WHERE name LIKE 'Orange'")

        # Confirm deletion
        print("Row deleted successfully!")
    else:
        print("No rows matched to deleted.")

    # Commit the changes
    conn.commit()

except sqlite3.Error as e:
    # Print error message if something goes wrong
    print(f"An error occurred: {e}")

finally:
    # Close the connection
    if conn:
        conn.close()
