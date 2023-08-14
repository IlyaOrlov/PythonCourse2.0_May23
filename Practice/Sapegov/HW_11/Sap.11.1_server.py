import threading
import socket


class ClientThread(threading.Thread):
    def __init__(self, conn, addr):
        super().__init__()
        self._connection = conn
        self._address = addr

    def run(self):
        print(f'Подключение адреса {self._address}')
        data = self._connection.recv(1024).decode().split(',')
        print(f'Принято: {data}')
        new_data = decoder(data)
        print(f'Отправлено: {new_data}')
        self._connection.send(','.join(new_data).encode())
        self._connection.close()
        print(f'Отключение адреса {self._address}')


class TcpServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self._socket = None
        self._running = False

    def run(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._socket.bind((self.host, self.port))
        self._socket.listen(1)
        self._running = True

        print('Сервер подключился')
        while self._running:
            conn, addr = self._socket.accept()
            ClientThread(conn, addr).start()

    def stop(self):
        self._running = False
        self._socket.close()
        print('Сервер отключился')


def decoder(lst):
    dic = {'ецнлос': 'солнце', 'анул': 'луна', 'ялмез': 'земля'}
    res = []
    for i in lst:
        res.append(dic[i])
    return res


if __name__ == '__main__':
    server = TcpServer(host='127.0.0.1', port=10000)
    try:
        server.run()
    except KeyboardInterrupt:
        server.stop()
