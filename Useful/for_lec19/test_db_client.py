from unittest import mock
import db_details


class TestDBClient:
    # рабочий вариант теста с патчингом БД для тестирования изолированного конструктора
    def test_dbclient_init(self):
        with mock.patch('db_details.sqlite3') as sqlite_mock:
            connection_mock = mock.Mock()
            sqlite_mock.connect.return_value = connection_mock
            sqlite_mock.Row = "fake_row"
            dbname = "fake_db"
            db_client = db_details.DBClient(dbname)
            sqlite_mock.connect.assert_called_once_with(dbname)
            assert db_client._conn.row_factory == sqlite_mock.Row

    # рабочий вариант теста DBClient в интеграции с БД
    def test_data_add(self):
        db_client = db_details.DBClient(":memory:")
        db_client.configure_db()
        id, name, price = 1, "Гайка", 50
        db_client.insert_detail(id, name, price)
        res = db_client.select_detail(id)
        assert res
        res_as_dict = dict(res)
        assert res_as_dict['Id'] == id
        assert res_as_dict['Name'] == name
        assert res_as_dict['Price'] == price


