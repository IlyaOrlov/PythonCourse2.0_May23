# Написать класс-обертку над SQLite (с возможностями менеджера контекста),
# которая может на вход принимать строки SQL запросов и возвращать данные в формате json. Класс должен иметь, как минимум, методы select и execute.

import sqlite3
import json

class SQLiteWrapper:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_name)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.connection:
            self.connection.close()

    def execute(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()
            return {"status": "success", "message": "Query executed successfully"}
        except sqlite3.Error as e:
            return {"status": "error", "message": str(e)}

    def select(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            columns = [col[0] for col in cursor.description]
            results = []
            for row in rows:
                results.append(dict(zip(columns, row)))
            return results
        except sqlite3.Error as e:
            return {"status": "error", "message": str(e)}

# Пример использования
db_name = "example.db"
query = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER);"

with SQLiteWrapper(db_name) as db:
    db.execute(query)

    insert_query = "INSERT INTO users (name, age) VALUES ('Alice', 25);"
    db.execute(insert_query)

    select_query = "SELECT * FROM users;"
    result = db.select(select_query)
    print(json.dumps(result, indent=2))
