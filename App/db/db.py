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

#creating products and inventory
product_cache = {}

for store_id, filename in store_files.items():
    path = os.path.join(DATA_FOLDER, filename)
    df = pd.read_csv(path)

    df.columns = [c.strip().lower() for c in df.columns]

    for _, row in df.iterrows():
        product_id = int(row["id"])
        product_name = str(row["name"])
        price = float(row["price"])
        stock = int(row["stock"])
        in_stock = stock > 0
        
        if product_id not in product_cache:
            cursor.execute(
                "INSERT IGNORE INTO products (product_id, product_name) VALUES (%s, %s)",
                (product_id, product_name)
            )
            product_cache[product_id] = True
            
            cursor.execute("""
            INSERT INTO inventory
            (store_id, product_id, price, stock, in_stock)
            VALUES (%s, %s, %s, %s, %s)
        """, (store_id, product_id, price, stock, in_stock))

conn.commit()

cursor.close()
conn.close()
print("Seeding complete.")