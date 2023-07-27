import sqlite3
import os


class DBClient:
    def __init__(self, dbname):
        self._conn = sqlite3.connect(dbname)
        self._conn.row_factory = sqlite3.Row
        print("Соединение открылось")

    def configure_db(self):
        cur = self._conn.cursor()

        # Создаем таблицу Details
        cur.execute("CREATE TABLE Details"
                    "    (Id        INTEGER    PRIMARY KEY  AUTOINCREMENT,"
                    "     Name      CHAR(128)  NOT NULL,"
                    "     Price     INTEGER   NOT NULL)")
        self._conn.commit()


    def insert_detail(self, id, name, price):
        cur = self._conn.cursor()
        cur.execute("INSERT INTO Details (Id, Name, Price)"
                    " VALUES (:id, :name, :price)",
                    {'id': id, 'name': name, 'price': price})
        self._conn.commit()


    def select_detail(self, detail_id):
        cur = self._conn.cursor()
        cur.execute("SELECT Id, Name, Price FROM Details WHERE Id = :detail_id",
                    {'detail_id': detail_id})
        return cur.fetchone()

    def __del__(self):
        self._conn.close()
        print("Соединение закрылось")


if __name__ == "__main__":
    db_name = "details.db"
    db_exists = os.path.exists(db_name)

    db_client = DBClient(db_name)

    if not db_exists:
        db_client.configure_db()

        db_client.insert_detail(1, "Гайка", 50)
        db_client.insert_detail(2, "Винт", 60)

    while i := input("Введите номер детали: "):
        num = int(i)
        res = db_client.select_detail(num)
        if res:
            print(dict(res))
        else:
            print(f"Нет детали с номером {i}")
