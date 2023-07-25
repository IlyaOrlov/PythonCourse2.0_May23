import sqlite3
import os


def configure_db(conn):
    cur = conn.cursor()

    # Создаем таблицу Details
    cur.execute("CREATE TABLE Details"
                "    (Id        INTEGER    PRIMARY KEY  AUTOINCREMENT,"
                "     Name      CHAR(128)  NOT NULL,"
                "     Price     INTEGER   NOT NULL)")


def insert_detail(conn, id, name, price):
    cur = conn.cursor()
    cur.execute("INSERT INTO Details (Id, Name, Price)"
                " VALUES (:id, :name, :price)",
                {'id': id, 'name': name, 'price': price})
    conn.commit()


def select_detail(conn, detail_id):
    cur = conn.cursor()
    cur.execute("SELECT Id, Name, Price FROM Details WHERE Id = :detail_id",
                {'detail_id': detail_id})
    return cur.fetchone()


if __name__ == "__main__":
    db_name = "details.db"
    db_exists = os.path.exists(db_name)

    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row
    if not db_exists:
        configure_db(conn)

        insert_detail(conn, 1, "Гайка", 50)
        insert_detail(conn, 2, "Винт", 60)

    while i := input("Введите номер детали: "):
        num = int(i)
        res = select_detail(conn, num)
        print(dict(res))
