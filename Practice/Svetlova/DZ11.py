#Запустите сервер, выполните команду: python server.py В другом окне запустите клиента: python client.py

import socket


def decrypt_words(words):
    dictionary = {
        "xlmrk": "apple",
        "vkrph": "banana",
        "jvsqf": "cherry"
        # Добавьте другие пары зашифрованное слово -> расшифрованное слово
    }

    decrypted_words = [dictionary[word] if word in dictionary else "Unknown" for word in words]
    return decrypted_words


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind(("127.0.0.1", 12345))
        server_socket.listen(1)

        print("Сервер запущен, ожидание подключения...")

        client_socket, client_address = server_socket.accept()
        print("Подключение от", client_address)

        received_data = client_socket.recv(1024).decode()
        encrypted_words = received_data.split(',')

        decrypted_words = decrypt_words(encrypted_words)
        response = ','.join(decrypted_words).encode()

        client_socket.send(response)
        # Закрываем сокет client_socket с помощью менеджера контекста
        client_socket.close()


if __name__ == "__main__":
    main()
