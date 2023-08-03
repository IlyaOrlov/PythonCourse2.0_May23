import socket

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 12345))

    encrypted_words = ["xlmrk", "vkrph", "jvsqf"]
    message = ','.join(encrypted_words).encode()

    client_socket.send(message)

    received_data = client_socket.recv(1024).decode()
    decrypted_words = received_data.split(',')

    print("Расшифрованные слова:", decrypted_words)

    client_socket.close()

if __name__ == "__main__":
    main()
    