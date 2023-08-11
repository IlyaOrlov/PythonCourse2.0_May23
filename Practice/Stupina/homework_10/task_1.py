from threading import Thread
import multiprocessing
import time


class MyThread(Thread):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y

    def run(self):
        find_primes(self.x, self.y)


def find_primes(start=3, end=None):
    if not end:
        if start < 3:
            raise ValueError
        else:
            end, start = start, 3

    if start < 0 or end < 0:
        print('Введите натуральное число')
        raise ValueError
    elif start > end:
        start, end = end, start

    s = set()

    if end >= 2:
        if start < 3:
            s.add(2)
            start = 3
    else:
        return None

    while start <= end:
        if start % 2 != 0:
            i = 3
            start_sqrt = start ** 0.5
            while i <= start_sqrt:
                if start % i == 0:
                    break
                i += 1
            else:
                s.add(start)
        start += 1
    return s


if __name__ == '__main__':
    t_start = time.perf_counter()
    arg = [(3, 10000), (10001, 20000), (20001, 30000)]

    for j in range(len(arg)):
        find_primes(*arg[j])
    print(find_primes(5,1))

    # lst_th = []
    # for j in range(len(arg)):
    #     th = MyThread(*arg[j])
    #     th.start()
    #     lst_th.append(th)
    # for t in lst_th:
    #     t.join()

    # lst_p = []
    # for j in range(len(arg)):
    #     p = multiprocessing.Process(target=find_primes, args=arg[j])
    #     p.start()
    #     lst_p.append(p)
    # for pr in lst_p:
    #     pr.join()

    t_ex = time.perf_counter() - t_start
    print(t_ex)
