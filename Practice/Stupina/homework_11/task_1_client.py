import socket
import pickle


class TCPClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self._socket = None

    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self._socket:
            self._socket.connect((self.host, self.port))
            data = ['У', 'Н', 'О', 'Д']
            self._socket.send(pickle.dumps(data))
            print('Запрос отправлен')
            res = self._socket.recv(1024)
            print(f'Ответ получен: {pickle.loads(res)}')


if __name__ == '__main__':
    client = TCPClient(host='127.0.0.1', port=6000)
    client.run()
