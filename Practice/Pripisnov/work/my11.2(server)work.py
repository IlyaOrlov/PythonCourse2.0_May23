import socket
import json


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(5)
    print("Сервер запущен и ждет подключения клиентов...")

    connected_users = {}  # Словарь для хранения информации о подключенных пользователях

    while True:
        conn, addr = server_socket.accept()
        print(f"Подключился клиент: {addr}")

        data = conn.recv(1024)
        user_info = json.loads(data.decode())
        username = user_info.get('name', 'Unknown')
        age = user_info.get('age', 'Unknown')

        # Добавляем информацию о пользователе в словарь connected_users
        connected_users[addr] = {'name': username, 'age': age}

        # Выводим информацию о подключенных пользователях
        print("Подключенные пользователи:")
        for addr, user in connected_users.items():
            print(f"IP: {addr[0]}, Port: {addr[1]}, Name: {user['name']}, Age: {user['age']}")

        conn.close()


if __name__ == "__main__":
    start_server()
