import os
import sqlite3

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "customers.db")


def get_customers():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    rows = conn.execute("SELECT customer_id, name, city FROM customers").fetchall()
    conn.close()
    return [dict(row) for row in rows]


def get_customer_by_id(customer_id: str):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    row = conn.execute(
        "SELECT customer_id, name, city FROM customers WHERE customer_id = ?",
        (customer_id,),
    ).fetchone()
    conn.close()
    if row is None:
        return None
    return dict(row)
