import sqlite3

# Create a new database
db_name = "HWSQL3.05.01.25.db"
conn = sqlite3.connect(db_name)
conn.row_factory = sqlite3.Row  # Access by column name

# Create a cursor
cursor = conn.cursor()

# Create a 'shopping' table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS shopping (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        amount INTEGER
    );
''')

# Commit changes and close the connection
conn.commit()
conn.close()

print(f"Database '{db_name}' created successfully!")

