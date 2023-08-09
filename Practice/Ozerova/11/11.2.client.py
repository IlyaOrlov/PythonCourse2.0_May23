import socket
import pickle

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def send_user_info(name, age):
    user = User(name, age)
    data = pickle.dumps(user)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', 12345))

    s.sendall(data)
    s.close()

if __name__ == '__main__':
    name = input('Введите имя пользователя: ')
    age = int(input('Введите возраст пользователя: '))
    send_user_info(name, age)
