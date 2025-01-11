import sqlite3

# connector
db_name: str = "18_12_2024db.db"
conn = sqlite3.connect(db_name) # creates a connector
conn.row_factory = sqlite3.Row # allow me to use column name

# cursor
cursor = conn.cursor()  # creates a cursor

#################### read from db

cursor.execute("SELECT * FROM sales")
row = cursor.fetchone()  # [ sql_obj, sql_obj ... ]
# result_list = [list(row) for row in rows]
#
# for result in result_list:
#     print(result)
print(row["product_name"])

conn.close()