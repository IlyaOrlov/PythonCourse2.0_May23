import threading
import socket
import pickle
import db_details


DB_NAME = "details.db"


class ClientThread(threading.Thread):
    def __init__(self, conn, addr):
        super().__init__()
        self._connection = conn
        self._address = addr

    def run(self):
        stop = False
        db_client = db_details.DBClient(DB_NAME)
        while not stop:
            request = self._connection.recv(1024)
            num = pickle.loads(request)
            if num == "stop":
                stop = True
            else:
                res = db_client.select_detail(num)
                if res:
                    data = dict(res)
                else:
                    data = f"Нет детали с номером {num}"
                self._connection.send(pickle.dumps(data))
        self._connection.close()


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
        self._socket.listen(5)
        self._running = True

        print('Server is up')
        while self._running:
            conn, addr = self._socket.accept()
            ClientThread(conn, addr).start()

    def stop(self):
        self._running = False
        self._socket.close()
        print('Server is down')


if __name__ == '__main__':
    srv = TcpServer(host='127.0.0.1', port=5555)
    try:
        srv.run()
    except KeyboardInterrupt:
        srv.stop()

