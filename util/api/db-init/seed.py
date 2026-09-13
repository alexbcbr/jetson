import sqlite3
import uuid
from faker import Faker
from init_db import init_db, DB_PATH

fake = Faker()


def seed():
    init_db()
    conn = sqlite3.connect(DB_PATH)
    for _ in range(10):
        conn.execute(
            "INSERT INTO customers (customer_id, name, city) VALUES (?, ?, ?)",
            (str(uuid.uuid4()), fake.name(), fake.city()),
        )
    for _ in range(5):
        conn.execute(
            "INSERT INTO products (name, price) VALUES (?, ?)",
            (fake.word().capitalize(), round(fake.pyfloat(min_value=1, max_value=500, right_digits=2), 2)),
        )
    conn.commit()
    conn.close()
    print("Seeded 10 customers and 5 products.")


if __name__ == "__main__":
    seed()
