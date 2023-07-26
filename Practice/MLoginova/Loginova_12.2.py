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

    # Создаем таблицу Customers
    cur.execute("CREATE TABLE Customers "
                "   (Purchase_id	INTEGER PRIMARY KEY  AUTOINCREMENT,"
                "    Product_id	INTEGER NOT NULL,"
	            "    Customer_name	CHAR(128) NOT NULL,"
	            "    Customer_surname	CHAR(128),"
	            "    Purchase_date	CHAR(8),"
	            "    FOREIGN KEY(product_id) REFERENCES Products(Product_id))")

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

    # Добавление записей в таблицу Customers
def insert_customers(conn, product_id, customer_name, surname, date_op):
    cur = conn.cursor()
    cur.execute("INSERT INTO Customers (Product_id, Customer_name, Customer_surname, Purchase_date )"
                " VALUES (:Product_id, :Customer_name, :Customer_surname, :Purchase_date)",
                {'Product_id': product_id, 'Customer_name': customer_name, 'Customer_surname': surname,
                 'Purchase_date': date_op})
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
    cur.execute("SELECT P.Product_name FROM Products as P WHERE P.Product_id not in (SELECT DISTINCT Product_id "
                "FROM Customers)")
    print("Товары, которые никто не покупал:")
    for row in cur:
        print(row)


if __name__ == "__main__":
    db_name = "shop.db"
    db_exists = os.path.exists(db_name)

    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row
    if not db_exists:
        configure_db(conn)

        insert_manufacturers(conn, "LG")
        insert_manufacturers(conn, "Samsung")
        insert_manufacturers(conn, "Haier")
        insert_products(conn, "Холодильник", 3)
        insert_products(conn, "Телевизор", 1)
        insert_products(conn, "Микроволновка", 2)
        insert_products(conn, "Телефон", 1)
        insert_customers(conn, 1, "Иван", "Иванов",  '15.05.23')
        insert_customers(conn, 2, "Пётр", "Петров",  '15.05.23')

    show_products_info(conn)
    print('/*********************************************************************************************************/')
    show_products_ostatok(conn)
    conn.close()
