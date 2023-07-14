import time


class MyTiming:
    def __enter__(self):
        self.start = time.time()

    def __exit__(self,exc_type, exc_val, exc_tb):
        self.end = time.time() - self.start
        print(f'Время исполнения кода {self.end} секунд')


with MyTiming():
    time.sleep(5)
