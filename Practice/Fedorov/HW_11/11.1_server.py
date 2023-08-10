# Написать клиентское и серверное приложения. Клиент отправляет на сервер список
# зашифрованных слов, сервер дешифрует слова по словарю и возвращает клиенту
# список расшифрованных слов. Клиент должен вывести полученный список.

import socket
import pickle

slovar = {1: "Дом", 2: "Квартира", 3: "Машина", 4: "Дача"}

def deshifrator(lst):
    res = []
    for i in lst:
        res.append(slovar.get(i))
    return res

if __name__ == "__main__"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "127.0.0.1"
    port = 12345
    s.bind((host, port))
    s.listen(5)
    while True:
        conn, addr = s.accept()
        data = pickle.loads(conn.recv(1024))
        print(f"Получено от клиента {addr} сообщение {data}")
        data = deshifrator(data)
        conn.send(pickle.dumps(data))
        conn.close()
    s.close()