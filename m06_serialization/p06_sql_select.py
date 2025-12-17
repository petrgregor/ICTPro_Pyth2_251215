import sqlite3

DB_NAME = "inventory.db"

print("--- 3. Select ---")

try:
    with sqlite3.connect(DB_NAME) as conn:
        query = """
            SELECT * FROM products;
        """
        cursor = conn.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        print(results)
        for result in results:
            id_, name, quantity, price = result
            print(f"PRODUCT: id={id_}, name={name}, quantity={quantity}, price={price}")
except Exception as e:
    print(f"ERROR: {e}")
