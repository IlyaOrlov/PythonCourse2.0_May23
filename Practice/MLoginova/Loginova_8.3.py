#  Напишите свой менеджер контекста, замеряющий и показывающий время исполнения кода внутри него.
from datetime import datetime as dt
import random


class TestTime:
    def __enter__(self):
        self.start_time = dt.now()
        print(f"Time begin: {self.start_time}")

    def __exit__(self, exc_type, exc_val, exc_tb):
        time_end = dt.now()
        print(f"Time end: {time_end}")
        res = time_end - self.start_time
        print(f'Время выполнения:{res}')


with TestTime():
    lst = [random.randint(-10, 100) for i in range(2000000)]
    print(lst)
