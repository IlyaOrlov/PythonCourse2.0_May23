# Напишите свой менеджер контекста, замеряющий и показывающий время исполнения кода внутри него.
import time


class Timer:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        work_time = time.time() - self.start_time
        print(f"Время выполнения кода: {work_time} секунд!")


def read_str(file):
    with open(file, 'r', encoding='utf-8') as f:
        for j in f:
            yield j


with Timer() as timer:
    time.sleep(2)
    file = read_str('reader_file.txt')
    for i in file:
        print(i)
