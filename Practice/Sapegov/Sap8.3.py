import time


class ContextManager:

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'Время выполнения кода: {time.time() - self.start} сек')


with ContextManager():
    i = 0
    x = 0
    while i < 10000:
        x += i ** 2
        i += 1
    print(x)
