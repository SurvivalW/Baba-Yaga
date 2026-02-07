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
    3: "Sam's_Club.csv",
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

#retriving column names from csv file
def pick_col(cols, candidates):
    """Return matching column name from candidates, else None."""
    for c in candidates:
        if c in cols:
            return c
    return None

product_cache = set()

#creating products and inventory
for store_id, filename in store_files.items():
    path = os.path.join(DATA_FOLDER, filename)
    df = pd.read_csv(path)

    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]
    df = df.loc[:, ~df.columns.str.startswith("unnamed")]  
    cols = set(df.columns)

    id_col = pick_col(cols, ["id", "product_id", "item_id", "sku"])
    name_col = pick_col(cols, ["name", "product_name", "item", "item_name", "title"])
    price_col = pick_col(cols, ["price", "cost", "unit_price"])
    stock_col = pick_col(cols, ["stock", "quantity", "qty", "inventory", "in_stock_count"])

    if not all([id_col, name_col, price_col, stock_col]):
        raise ValueError(
            f"{filename} columns not recognized.\n"
            f"Found: {sorted(list(cols))}\n"
            f"Need something like id/name/price/stock."
        )

    