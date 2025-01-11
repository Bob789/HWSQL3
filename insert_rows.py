import sqlite3

try:
    # Create a new database
    db_name = "HWSQL3.05.01.25.db"
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row  # Access by column name

    # Create a cursor
    cursor = conn.cursor()

    # Insert multiple rows using a list of tuples
    data_to_insert = [
        (1, 'Avokado', 5),
        (2, 'Milk', 2),
        (3, 'Bread', 3),
        (4, 'Chocolate', 8),
        (5, 'Bamba', 5),
        (6, 'Orange', 10),
    ]

    # Use executemany to insert multiple rows at once
    cursor.executemany('''
        INSERT INTO shopping (id, name, amount)
        VALUES (?, ?, ?)
    ''', data_to_insert)

    # Commit changes
    conn.commit()

    # Print success message
    print("Data inserted successfully!")

except sqlite3.Error as e:
    # Print error message if something goes wrong
    print(f"An error occurred: {e}")

finally:
    # Close the connection
    if conn:
        conn.close()
