from threading import Thread
import multiprocessing
import time


def find_primes(start=3, end=None):
    if not end:
        end, start = start, 3
    s = set()
    while start <= end:
        if start % 2 == 0 or start == 1 or start == 0:
            if start == 2:
                s.add(start)
        else:
            i = 3
            start_sqrt = start ** 0.5
            while i <= start_sqrt:
                if start % i == 0:
                    break
                i += 1
            else:
                s.add(start)
        start += 1
    print(s)
    return s


class MyThread(Thread):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y

    def run(self):
        find_primes(self.x, self.y)


if __name__ == '__main__':
    t_start = time.perf_counter()
    arg = [(3, 10000), (10001, 20000), (20001, 30000)]

    # for j in range(len(arg)):
    #     find_primes(*arg[j])

    # lst_th = []
    # for j in range(len(arg)):
    #     th = MyThread(*arg[j])
    #     th.start()
    #     lst_th.append(th)
    # for t in lst_th:
    #     t.join()

    lst_p = []
    for j in range(len(arg)):
        p = multiprocessing.Process(target=find_primes, args=arg[j])
        p.start()
        lst_p.append(p)
    for pr in lst_p:
        pr.join()

    t_ex = time.perf_counter() - t_start
    print(t_ex)
