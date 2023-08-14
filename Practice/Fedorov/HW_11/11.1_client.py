import socket
import pickle

slova = [1, 2, 3]

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    host = '127.0.0.1'
    port = 12345
    s.connect((host, port))
    s.sendall(pickle.dumps(slova))
    d = s.recv(1024)
    while d:
        print(pickle.loads(d))
        d = s.recv(1024)
