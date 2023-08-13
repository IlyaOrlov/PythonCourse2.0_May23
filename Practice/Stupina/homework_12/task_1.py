# Написать класс-обертку над SQLite (с возможностями менеджера контекста),
# которая может на вход принимать строки SQL запросов и возвращать данные в формате json.
# Класс должен иметь, как минимум, методы select и execute.

import sqlite3
import json
import os


class MyDB:
    def __init__(self, dbname):
        self.dbname = dbname

    def __enter__(self):
        self._conn = sqlite3.connect(self.dbname)
        self._conn.row_factory = sqlite3.Row
        print("Соединение открылось")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._conn.close()
        print("Соединение закрылось")

    def select(self, req):
        cur = self._conn.cursor()
        cur.execute(req)

        s = set()
        for row in cur:
            s.add(json.dumps(dict(row), sort_keys=True, indent=4))
        return s

    def execute(self, req):
        cur = self._conn.cursor()
        cur.execute(req)
        self._conn.commit()


if __name__ == '__main__':
    db_name = 'db_Product.db'
    db_exists = os.path.exists(db_name)
    with MyDB(db_name) as db:
        if not db_exists:
            s = 'CREATE TABLE Product (Article INTEGER PRIMARY KEY, Title CHAR(128) NOT NULL, ' \
                'Model CHAR(128) NOT NULL, Price INTEGER NOT NULL)'
            db.execute(s)
            s = 'INSERT INTO Product (Article, Title, Model, Price) VALUES (111, "Платье", "летнее", 3000)'
            db.execute(s)
            s = 'INSERT INTO Product (Article, Title, Model, Price) VALUES (113, "Платье", "вечернее", 15000)'
            db.execute(s)
            s = 'INSERT INTO Product (Article, Title, Model, Price) VALUES (200, "Брюки", "клеш", 5000)'
            db.execute(s)

        print('Запрос: * FROM Product')
        s = 'SELECT * FROM Product'
        res_select = db.select(s)
        [print(json.loads(i)) for i in res_select]

        s = 'SELECT * FROM Product WHERE Title = "Платье" '
        res_select = db.select(s)
        print('Запрос: Title = Платье')
        [print(json.loads(i)) for i in res_select]

        s = 'SELECT * FROM Product WHERE Price > 10000 '
        res_select = db.select(s)
        print('Запрос: Price > 10000')
        [print(json.loads(i)) for i in res_select]

