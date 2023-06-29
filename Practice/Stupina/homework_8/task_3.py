import time


class TimeManager:
    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop = time.time() - self.start
        print(f'Время работы программы: {self.stop} сек.')


with TimeManager():
    lst = range(1, 1000000)
    for i in lst:
        i += 1
