#  Напишите свой менеджер контекста, замеряющий и показывающий время исполнения кода внутри него.
from datetime import datetime
import random


class TestTime:
    def __enter__(self):
        self.start_time = datetime.now()
        print(f"Time begin: {self.start_time}")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Time end: {datetime.now()}")
        print(f'Время выполнения:{datetime.now() - self.start_time}')


with TestTime():
    lst = [random.randint(-10, 100) for i in range(2000000)]
    print(lst)
