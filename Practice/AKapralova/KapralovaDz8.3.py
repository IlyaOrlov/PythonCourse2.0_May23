# Напишите свой менеджер контекста, замеряющий и показывающий время исполнения кода внутри него.
import time


class Timer:
    def __enter__(self):
        self.start_time = time.time()

    def __exit__(self, exc_type, exc_value, traceback):
        elapsed_time = time.time() - self.start_time
        print(f"Время работы программы: {elapsed_time} сек.")


with Timer():
    # lst = [1, 3, 24, 2, 3, 7]
    # lst.sort()
    # print(lst)
    enumerated_numbers = enumerate(list(range(1, 10001)))
    for i, j in enumerated_numbers:
        print(i, j)
