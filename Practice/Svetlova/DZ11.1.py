import socket


def main():
    encrypted_words = ["xlmrk", "vkrph", "jvsqf"]

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect(("127.0.0.1", 12345))

        message = ','.join(encrypted_words).encode()
        client_socket.send(message)

        received_data = client_socket.recv(1024).decode()
        decrypted_words = received_data.split(',')

        print("Расшифрованные слова:", decrypted_words)


if __name__ == "__main__":
    main()
