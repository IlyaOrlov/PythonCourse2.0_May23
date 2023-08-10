import sqlite3


class DB:

    def __init__(self, name):
        self.conn = sqlite3.connect(name)

    def execute(self, sql):
        self.conn.execute(sql)
        self.conn.commit()

    def select(self, sql):
        cursor = self.conn.cursor()
        cursor.row_factory = sqlite3.Row
        cursor.execute(sql)
        for row in cursor:
            print(dict(row))

    def __del__(self):
        self.conn.close()


x = DB('bla.db')

x.execute("INSERT INTO FLE (ID, NAME, AGE, ADDRESS, SALARY) "
          "VALUES (1, 'Paul', 32, 'California', 20000.00)")
x.execute("INSERT INTO FLE (ID, NAME, AGE, ADDRESS, SALARY) "
          "VALUES (2, 'Allen', 25, 'Texas', 25000.00)")
x.execute("INSERT INTO FLE (ID, NAME, AGE, ADDRESS, SALARY) "
          "VALUES (3, 'Teddy', 23, 'Norway', 20000.00)")
x.execute('UPDATE FLE set salary = 25000.00 WHERE id = 1')
x.execute('DELETE from FLE where id=2;')
x.select('SELECT id, name, address, salary from FLE WHERE id = 1')
x.select('SELECT * from FLE')
