import os.path
import sqlite3

DB_NAME = "inventory.db"

print("--- 1. Setup: connection and Creating table ---")

# pokud soubor existuje, tak ho smažeme
if os.path.exists(DB_NAME):
    os.remove(DB_NAME)

try:
    with sqlite3.connect(DB_NAME) as conn:
        create_table_query = """
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                quantity INTEGER NOT NULL,
                price REAL
            );
        """
        cursor = conn.cursor()
        cursor.execute(create_table_query)
        print("Table 'products' created successfully.")
except Exception as e:
    print(f"ERROR: {e}")
