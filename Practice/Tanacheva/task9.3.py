import time


class TestManager:

    def __enter__(self):
        self.start_time = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Время исполнения функции: {time.time() - self.start_time}")


with TestManager():
    for i in range(100000):
        print(i)
