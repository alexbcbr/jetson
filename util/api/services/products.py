import os
import sqlite3

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "customers.db")


def get_product_by_id(product_id: int):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    row = conn.execute(
        "SELECT id, name, price FROM products WHERE id = ?",
        (product_id,),
    ).fetchone()
    conn.close()
    if row is None:
        return None
    return dict(row)
