import time
from itertools import filterfalse


class Timer:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        work_time = time.time() - self.start_time
        print(f"Время выполнения кода: {work_time} секунд!")


def fun2(arr):
    lst = []
    for i in arr:
        if len(i) >= 5:
            lst.append(i)
    return lst


def fun3(arr):
    return list(filterfalse(check, arr))


def check(x):
    return len(x) < 5


with Timer() as timer:
    time.sleep(1)
    lst = ['hello', 'i', 'write', 'cool', 'code']
    k = fun2(lst)
    print(f"Результат 1 задания: функция возвращает >>> {k}")

with Timer() as timer:
    time.sleep(1)
    lst = ['hello', 'i', 'write', 'cool', 'code']
    g = fun3(lst)
    print(f"Результат 1 задания: функция возвращает >>> {g}")