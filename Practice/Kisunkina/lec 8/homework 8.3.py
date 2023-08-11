# Напишите свой менеджер контекста, замеряющий и показывающий время исполнения кода внутри него.

import time

class Timer:
    def __enter__(self):
        self.start_time = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        end_time = time.time()
        print(f"Время исполнения кода: {end_time - self.start_time} секунд")


with Timer():
    lst = range(1, 1000000)
    for i in lst:
        i +=1
