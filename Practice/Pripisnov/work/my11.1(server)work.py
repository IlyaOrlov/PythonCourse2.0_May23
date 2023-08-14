import socket


# Словарь для дешифровки слов
dictionary = {
    'xofa': 'Привет',
    'ymno': 'Проверил',
    'zijk': 'Отлично'
}


def decrypt_words(encrypted_words):
    decrypted_words = [dictionary.get(word, 'Unknown word') for word in encrypted_words]
    return decrypted_words


def main():
    host = '127.0.0.1'
    port = 12345

    # Создаем сокет и связываем его с хостом и портом
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))

    # Слушаем подключения от клиентов
    server_socket.listen(1)
    print('Сервер запущен. Ожидание подключения клиента...')

    # Принимаем подключение клиента
    client_socket, client_address = server_socket.accept()
    print('Подключен клиент:', client_address)

    # Получаем данные от клиента (список зашифрованных слов)
    data = client_socket.recv(1024).decode()
    encrypted_words = data.split(',')

    # Дешифруем слова и получаем список расшифрованных слов
    decrypted_words = decrypt_words(encrypted_words)

    # Отправляем список расшифрованных слов клиенту
    response = ','.join(decrypted_words)
    client_socket.sendall(response.encode())

    # Закрываем соединение с клиентом
    client_socket.close()
    server_socket.close()


if __name__ == '__main__':
    main()
