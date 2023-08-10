import socket
import pickle
import random
import time


class TcpClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self._socket = None

    def run(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.connect((self.host, self.port))
        while i := input("Введите номер детали (или stop): "):
            if i == "stop":
                self._socket.send(pickle.dumps(i))
                break
            else:
                num = int(i)
                self._socket.send(pickle.dumps(num))
                data = self._socket.recv(1024)
                print(f'Received: {pickle.loads(data)}')
        self._socket.close()


if __name__ == '__main__':
    myclient = TcpClient(host='127.0.0.1', port=5555)
    myclient.run()