from threading import Thread
import time


def find_primes(start, end):
    lst = []
    for i in range(start, end+1):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                lst.append(i)
    print(lst)


if __name__ == '__main__':
    start_time = time.perf_counter()
    thr1 = Thread(target=find_primes, args=(3, 10000))
    thr2 = Thread(target=find_primes, args=(10001, 20000))
    thr3 = Thread(target=find_primes, args=(20001, 30000))
    threads = [thr1, thr2, thr3]
    for i in threads:
        i.start()
    for i in threads:
        i.join()

    end_time = time.perf_counter() - start_time
    print(f"Затраченное время {end_time}")
