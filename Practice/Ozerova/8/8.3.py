import time


class MyTiming:
    def __enter__(self):
        self.start = time.time()

    def __exit__(self,exc_type, exc_val, exc_tb):
        print(f'Время исполнения кода {time.time() - self.start} секунд')


with MyTiming():
    time.sleep(5)
