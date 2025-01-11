import sqlite3

# Connect to the database
db_name: str = "18_12_2024db.db"
conn = sqlite3.connect(db_name)
conn.row_factory = sqlite3.Row  # Access by column name

# Create a cursor
cursor = conn.cursor()

# Execute the query to get all product names
cursor.execute("SELECT product_name FROM sales")
rows = cursor.fetchall()

# Extract the product names
product_names = [row["product_name"] for row in rows]

# Print the product names
for name in product_names:
    print(name)

# Close the connection
conn.close()
