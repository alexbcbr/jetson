import sqlite3
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from services import customers

SCHEMA = """
    CREATE TABLE customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id TEXT NOT NULL UNIQUE,
        name TEXT,
        city TEXT
    )
"""


def _seed_db(path):
    conn = sqlite3.connect(path)
    conn.execute(SCHEMA)
    conn.execute(
        "INSERT INTO customers (customer_id, name, city) VALUES ('cust-001', 'Alice', 'Toronto')"
    )
    conn.execute(
        "INSERT INTO customers (customer_id, name, city) VALUES ('cust-002', 'Bob', 'London')"
    )
    conn.commit()
    conn.close()


def test_get_customers(tmp_path, monkeypatch):
    test_db = str(tmp_path / "test.db")
    monkeypatch.setattr(customers, "DB_PATH", test_db)
    _seed_db(test_db)

    result = customers.get_customers()

    assert len(result) == 2
    assert result[0]["customer_id"] == "cust-001"
    assert result[0]["name"] == "Alice"
    assert result[0]["city"] == "Toronto"
    assert result[1]["customer_id"] == "cust-002"
    assert result[1]["name"] == "Bob"
    assert result[1]["city"] == "London"


def test_get_customer_by_id(tmp_path, monkeypatch):
    test_db = str(tmp_path / "test.db")
    monkeypatch.setattr(customers, "DB_PATH", test_db)
    _seed_db(test_db)

    result = customers.get_customer_by_id("cust-001")

    assert result is not None
    assert result["customer_id"] == "cust-001"
    assert result["name"] == "Alice"
    assert result["city"] == "Toronto"


def test_get_customer_by_id_not_found(tmp_path, monkeypatch):
    test_db = str(tmp_path / "test.db")
    monkeypatch.setattr(customers, "DB_PATH", test_db)
    _seed_db(test_db)

    result = customers.get_customer_by_id("nonexistent")

    assert result is None
