from threading import Thread
import time
from fun_10 import find_primes


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
