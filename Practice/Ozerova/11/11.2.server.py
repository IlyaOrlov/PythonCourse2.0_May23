import socket
import pickle

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def receive_user_info():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('localhost', 12345))
    s.listen(5)

    while True:
        conn, addr = s.accept()

        data = conn.recv(1024)

        if not data:
            break

        user = pickle.loads(data)

        print(f'Имя пользователя: {user.name}')
        print(f'Возраст пользователя: {user.age}')

        conn.close()

if __name__ == '__main__':
    receive_user_info()