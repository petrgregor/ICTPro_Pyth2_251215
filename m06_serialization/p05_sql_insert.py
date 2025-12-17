import sqlite3

DB_NAME = "inventory.db"

print("--- 2. Insert into ---")

try:
    with sqlite3.connect(DB_NAME) as conn:
        query = """
            INSERT INTO products (name, quantity, price)
                VALUES ('product1', 5, 12.5);
        """
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
except Exception as e:
    print(f"ERROR: {e}")
