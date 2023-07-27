import sqlite3
import os


def configure_db(conn):
    cur = conn.cursor()

    # Создаем таблицу Manufacturers
    cur.execute("CREATE TABLE Manufacturers"
                "    (Manufacturer_id        INTEGER    PRIMARY KEY  AUTOINCREMENT,"
                "     Manufacturer_name      CHAR(128)  NOT NULL)")

    # Создаем таблицу Products
    cur.execute("CREATE TABLE Products"
                "    (Product_id        INTEGER    PRIMARY KEY  AUTOINCREMENT,"
                "     Product_name      CHAR(128)  NOT NULL,"
                "     Manufacturer_id   INTEGER,"
                "     FOREIGN KEY(Manufacturer_id) REFERENCES Manufacturers(Manufacturer_id))")

    # Создаем таблицу Clients
    cur.execute("CREATE TABLE Clients "
                "   (Client_id	INTEGER PRIMARY KEY  AUTOINCREMENT,"
                "    Client_name	CHAR(128) NOT NULL,"
                "    Client_surname	CHAR(128))")

    # Создаем таблицу Purchases
    cur.execute("CREATE TABLE Purchases "
                "   (Purchase_id	INTEGER PRIMARY KEY  AUTOINCREMENT,"
                "    Product_id	INTEGER NOT NULL,"
	            "    Client_id INTEGER NOT NULL,"
	            "    Purchase_date	CHAR(8),"
	            "    FOREIGN KEY(product_id) REFERENCES Products(Product_id),"
                "    FOREIGN KEY(Client_id) REFERENCES Clients(Client_id))")

# Добавление записей в таблицу Manufacturers
def insert_manufacturers(conn, name):
    cur = conn.cursor()
    cur.execute("INSERT INTO Manufacturers (Manufacturer_name)"
                " VALUES (:Manufacturer_name)",
                {'Manufacturer_name': name})
    conn.commit()

# Добавление записей в таблицу Products
def insert_products(conn, name, id):
    cur = conn.cursor()
    cur.execute("INSERT INTO Products (Product_name, Manufacturer_id)"
                " VALUES (:Product_name, :Manufacturer_id)",
                {'Product_name': name, 'Manufacturer_id': id})
    conn.commit()

# Добавление записей в таблицу Clients
def insert_clients(conn, name, surname):
    cur = conn.cursor()
    cur.execute("INSERT INTO Clients (Client_name, Client_surname)"
                " VALUES (:Client_name, :Client_surname)",
                {'Client_name': name, 'Client_surname': surname})
    conn.commit()

    # Добавление записей в таблицу Purchases
def insert_purchases(conn, product_id, client_id, date_op):
    cur = conn.cursor()
    cur.execute("INSERT INTO Purchases (Product_id, Client_id, Purchase_date )"
                " VALUES (:Product_id, :Client_id, :Purchase_date)",
                {'Product_id': product_id, 'Client_id': client_id, 'Purchase_date': date_op})
    conn.commit()

# Вывод информации о всех товарах с указанием информации о производителе
def show_products_info(conn):
    cur = conn.cursor()
    cur.execute("SELECT P.Product_name, M.Manufacturer_name"
                " FROM Products as P, Manufacturers as M "
                " WHERE P. Manufacturer_id = M. Manufacturer_id")
    print("Товары и их производители:")
    for row in cur.fetchall():
        print(dict(row))

# Вывод информации о всех товарах, которые никто не покупал
def show_products_ostatok(conn):
    cur = conn.cursor()
    cur.row_factory = None
    cur.execute("SELECT Pr.Product_id, Pr.Product_name FROM Products as Pr left join Purchases as P "
                "on Pr.Product_id = P.Product_id where p.Purchase_id is null")
    print("Товары, которые никто не покупал:")
    for row in cur:
        print(row)


if __name__ == "__main__":
    db_name = "shop.db"
    db_exists = os.path.exists(db_name)

    with (sqlite3.connect(db_name)) as db:
        db.row_factory = sqlite3.Row
        if not db_exists:
            configure_db(db)

            insert_manufacturers(db, "LG")
            insert_manufacturers(db, "Samsung")
            insert_manufacturers(db, "Haier")
            insert_products(db, "Холодильник", 3)
            insert_products(db, "Телевизор", 1)
            insert_products(db, "Микроволновка", 2)
            insert_products(db, "Телефон", 1)
            insert_clients(db, "Иван", "Иванов")
            insert_clients(db, "Пётр", "Петров")
            insert_purchases(db, 1, 1,  '15.05.23')
            insert_purchases(db, 2, 2,  '15.05.23')

        show_products_info(db)
        print('/*********************************************************************************************************/')
        show_products_ostatok(db)
