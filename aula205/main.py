import sqlite3
from pathlib import Path


ROOT_DIR = Path(__file__).parent
DB_NAME = "db.sqlite3"
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = "custumers"


connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute(
    f"CREATE TABLE IF NOT EXISTS {TABLE_NAME}"
    "("
    "id INTEGER PRIMARY KEY AUTOINCREMENT,"
    "name TEXT,"
    "weight REAL"
    ")"
)
connection.commit()

cursor.execute(f"insert into {TABLE_NAME} (id, name, weight) VALUES (NULL, 'Marcia', 42)")
connection.commit()


cursor.close()
connection.close()
