import sqlite3

try:
    # Connect to the database
    db_name = "HWSQL3.05.01.25.db"
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row  # Access by column name

    # Create a cursor
    cursor = conn.cursor()

    # Select rows to COUNT
    cursor.execute("SELECT COUNT(*) FROM shopping")
    rows_count = cursor.fetchone()[0]

    if rows_count:
        # Display rows number
        print(f"Rows number: {rows_count}")
    else:
        print("No rows .")

except sqlite3.Error as e:
    # Print error message if something goes wrong
    print(f"An error occurred: {e}")

finally:
    # Close the connection
    if conn:
        conn.close()
