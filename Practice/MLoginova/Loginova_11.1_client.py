import socket

def client_socket():
    words = ['кот', 'собака', 'попугай', 'харёк']

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cl:
        host = '127.0.0.1'
        port = 23561
        cl.connect((host, port))
        cl.send(','.join(words).encode())
        new_words = cl.recv(1024).decode().split(',')
        print(f"Cписок расшифрованных слов: {new_words}")


if __name__ == "__main__":
    client_socket()
