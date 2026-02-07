import os
import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    port = 3307,
    user = "root",
    password = "ishaSalvatore@1974",
    database = "groceryApp"
)

cursor = conn.cursor()

DATA_FOLDER = os.path.join(os.getcwd(), "MakingData")

store_files = {
    1: "Kroger.csv",
    2: "Meijer.csv",
    3: "Sam's Club.csv",
    4: "Target.csv",
    5: "Walmart.csv"
}

#inserting values into stores
for store_id, filename in store_files.items():
    store_name = filename.replace(".csv", "")
    cursor.execute(
        "INSERT IGNORE INTO stores (store_id, store_name) VALUES (%s, %s)",
        (store_id, store_name)
    )

conn.commit()