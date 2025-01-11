import sqlite3

# Connect to the database
db_name: str = "18_12_2024db.db"
conn = sqlite3.connect(db_name)
conn.row_factory = sqlite3.Row  # Access by column name

# Create a cursor
cursor = conn.cursor()

# Execute a query to get the product with ID 2
cursor.execute("SELECT product_name FROM sales WHERE id = 2")
row = cursor.fetchone()

# Print the product name
if row:
    print(row["product_name"])

# Close the connection
conn.close()
