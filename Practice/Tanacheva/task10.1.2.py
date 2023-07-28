from threading import Thread
import time


def find_primes(start, end):
    lst = []
    for i in range(start, end+1):
        for j in lst:
            if i % j == 0:
                break
        else:
            lst.append(i)
    print(lst)


if __name__ == '__main__':
    start_time = time.perf_counter()
    tread1 = Thread(target=find_primes, args=(3, 10000))
    tread2 = Thread(target=find_primes, args=(10001, 20000))
    tread3 = Thread(target=find_primes, args=(20001, 30000))
    tread1.start()
    tread2.start()
    tread3.start()
    tread1.join()
    tread2.join()
    tread3.join()
    end_time = time.perf_counter() - start_time
    print(f"Затраченное время {end_time}")
