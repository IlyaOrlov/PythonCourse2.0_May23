import socket


def main():
    host = '127.0.0.1'
    port = 12345

    # Список зашифрованных слов
    encrypted_words = ['xofa', 'ymno', 'zijk']

    # Создаем сокет и подключаемся к серверу
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    # Отправляем список зашифрованных слов серверу
    data = ','.join(encrypted_words)
    client_socket.sendall(data.encode())

    # Получаем список расшифрованных слов от сервера
    response = client_socket.recv(1024).decode()
    decrypted_words = response.split(',')

    print("Расшифрованные слова:")
    for word in decrypted_words:
        print(word)

    # Закрываем соединение с сервером
    client_socket.close()


if __name__ == '__main__':
    main()
