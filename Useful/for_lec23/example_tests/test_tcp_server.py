"""Написать Unit-тесты для TCP-сервера (код см. далее),
использовать mock, чтобы эмулировать действия клиента и создание потоков,
получить code coverage репорт в html формате."""

import tcp_server
import unittest
from unittest import mock
from itertools import tee


class TestTcpServer(unittest.TestCase):
    def test_tcpserver(self):
        # Создаём объект тестируемого класса.
        server = tcp_server.TcpServer(host='localhost', port=1234)

        # Заменяем зависимости на mock-объекты
        tcp_server.socket = mock.Mock()
        tcp_server.ClientThread = mock.Mock()

        # Настраиваем поведение mock-объекта socket.socket
        socket_mock = mock.Mock()
        hosts = [('ip1', 'port1'), ('ip2', 'port2'), ('ip3', 'port3'), StopIteration]
        socket_mock.accept.side_effect = hosts
        tcp_server.socket.socket.return_value = socket_mock

        # Настраиваем поведение mock-объекта tcp_server.ClientThread
        def thread_start():
            ip, port = hosts[socket_mock.accept.call_count - 1]
            print(f"New client connect - {ip}:{port}")
        client_mock = mock.Mock()
        client_mock.start.side_effect = thread_start
        tcp_server.ClientThread.return_value = client_mock

        # Тестируем и выполняем проверки
        try:
            self.assertFalse(server._runnning)
            server.run()
            self.assertTrue(server._runnning)
        except StopIteration:
            server.stop()
            self.assertFalse(server._runnning)

        assert socket_mock.accept.call_count == 4
        assert client_mock.start.call_count == 3


if __name__ == '__main__':
    unittest.main()
