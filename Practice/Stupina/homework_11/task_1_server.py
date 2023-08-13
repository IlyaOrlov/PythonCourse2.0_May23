import socket
import threading
import pickle


class ClientThread(threading.Thread):
    def __init__(self, conn):
        super().__init__()
        self._c = conn

    def run(self):
        data = self._c.recv(1024)
        data = pickle.loads(data)
        print(f'Принято сообщение: {data}')
        res = my_key(data)
        self._c.send(pickle.dumps(res))
        print('Ответ отправлен')


class TCPServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self._socket = None
        self.__running = False

    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self._socket:
            self._socket.bind((self.host, self.port))
            self._socket.listen(6)
            self.__running = True
            print('Сервер запущен')
            while self.__running:
                print('Ожидание клиента')
                conn, ad = self._socket.accept()
                with conn:
                    print('Клиент принят')
                    ClientThread(conn).start()


def my_key(d):
    key = {'У': 'Уж', 'Н': 'небо', 'О': 'осенью', 'Д': 'дышало'}
    res = []
    for i in d:
        res.append(key[i])
    return res


if __name__ == '__main__':

    server = TCPServer(host='127.0.0.1', port=6000)
    server.run()
