import socket


def decoder(words):
    dictionary = {"собака": "Рекс", "хомяк": "Кузя", "кот": "Барсик"}
    d_words = []
    for i in dictionary:
        d_words.append(dictionary.get(i))
    return d_words

def server_socket():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        host = '127.0.0.1'
        port = 23561
        s.bind((host, port))
        s.listen(1)
        cl, addr = s.accept()
        print(f"Сервер получил соединение от {addr}")
        with cl:
            decode_words = cl.recv(1024).decode().split(',')
            decoder_words = decoder(decode_words)
            #  print(f"{decoder_words}")
            encode_words = ','.join(decoder_words).encode()
            cl.send(encode_words)


if __name__ == "__main__":
    server_socket()
