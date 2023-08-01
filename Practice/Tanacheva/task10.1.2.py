from threading import Thread
from math import sqrt
import time


def find_primes(start, end):
    lst = []
    if start > 1:
        for i in range(start, end+1):
            for j in range(2, int(sqrt(i))+1):
                if j > int((sqrt(i))+1):
                    lst.append(i)
                    break
                if i % j == 0:
                    break
            else:
                lst.append(i)
    print(lst)


if __name__ == '__main__':
    start_time = time.perf_counter()
    threads = []
    for args in ((3, 10000), (10001, 20000), (20001, 30000)):
        thr = Thread(target=find_primes, args=args)
        thr.start()
        threads.append(thr)
    for i in threads:
        i.join()

    end_time = time.perf_counter() - start_time
    print(f"Затраченное время {end_time}")
