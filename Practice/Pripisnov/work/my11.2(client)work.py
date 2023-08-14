import socket
import json


def send_user_info(username, age):
    user_info = {'name': username, 'age': age}
    message = json.dumps(user_info).encode()

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))
    client_socket.send(message)
    client_socket.close()


if __name__ == "__main__":
    # Примеры запуска клиентского приложения с различными пользователями
    send_user_info('Alice', 25)
    send_user_info('Bob', 30)
    send_user_info('Eve', 22)
