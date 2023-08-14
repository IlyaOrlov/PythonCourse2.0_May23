import socket


class TcpClient:
    def __init__(self, host, port, message):
        self.host = host
        self.port = port
        self.message = message
        self._socket = None

    def run(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.connect((self.host, self.port))
        self._socket.send(self.message.encode())
        data = self._socket.recv(1024)
        print(f'Расшифрованный список: {data.decode().split(",")}')
        self._socket.close()


if __name__ == '__main__':
    lst = ['ецнлос', 'анул', 'ялмез']
    lst_join = ','.join(lst)
    client = TcpClient(host='127.0.0.1', port=10000, message=lst_join)
    client.run()
