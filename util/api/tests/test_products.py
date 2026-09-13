import sqlite3
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from services import products

SCHEMA = """
    CREATE TABLE products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL NOT NULL
    )
"""


def _seed_db(path):
    conn = sqlite3.connect(path)
    conn.execute(SCHEMA)
    conn.execute(
        "INSERT INTO products (name, price) VALUES ('Widget', 19.99)"
    )
    conn.execute(
        "INSERT INTO products (name, price) VALUES ('Gadget', 49.95)"
    )
    conn.commit()
    conn.close()


def test_get_product_by_id(tmp_path, monkeypatch):
    test_db = str(tmp_path / "test.db")
    monkeypatch.setattr(products, "DB_PATH", test_db)
    _seed_db(test_db)

    result = products.get_product_by_id(1)

    assert result is not None
    assert result["id"] == 1
    assert result["name"] == "Widget"
    assert result["price"] == 19.99


def test_get_product_by_id_not_found(tmp_path, monkeypatch):
    test_db = str(tmp_path / "test.db")
    monkeypatch.setattr(products, "DB_PATH", test_db)
    _seed_db(test_db)

    result = products.get_product_by_id(999)

    assert result is None
