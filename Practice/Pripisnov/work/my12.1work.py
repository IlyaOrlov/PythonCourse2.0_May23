import sqlite3
import json


class SQLiteWrapper:

    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

    def execute(self, query, params=None):
        self.cursor.execute(query, params or ())
        self.connection.commit()

    def select(self, query, params=None):
        self.cursor.execute(query, params or ())
        rows = self.cursor.fetchall()
        columns = [desc[0] for desc in self.cursor.description]
        results = [dict(zip(columns, row)) for row in rows]
        return json.dumps(results, indent=4)

# Пример использования:
db_name = 'example.db'

# Создаем таблицу и вставляем данные
with SQLiteWrapper(db_name) as db:
    db.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
    db.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Alice', 30))
    db.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Bob', 25))

# Выбираем и выводим данные в формате JSON
with SQLiteWrapper(db_name) as db:
    select_query = "SELECT * FROM users WHERE age > ?"
    json_result = db.select(select_query, (26,))
    print(json_result)
