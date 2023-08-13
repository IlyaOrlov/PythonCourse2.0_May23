# Написать функцию find_primes(start, end), которая ищет все простые числа
# в диапазоне от заданного числа start (по умолчанию 3) до заданного числа end. Далее необходимо:
# Запустить ее три раза последовательно в диапазоне от 3 до 10000, от 10001 до 20000, от 20001 до 30000.
# Запустить ее три раза с теми же аргументами, но каждый раз в отдельном потоке с помощью threading.
# Thread. Что будет, если 'забыть' выполнить start или join для потоков?
# Запустить ее три раза с теми же аргументами, но каждый раз в отдельном процессе с помощью
# multiprocessing.Process. Что будет, если 'забыть' выполнить start или join для процессов?
# Замерить время исполнения каждого варианта и сравнить результаты.
import time
import threading
import multiprocessing


def isPrime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


def isPrimeon(n):
    d = 2
    while n % d != 0:
        d += 1
    return d == n


def find_primes(start, end):
    res = []
    while start < end:
        if isPrimeon(start):
            res.append(start)
        start += 1
    return res

if __name__ == '__main__':
    start_time = time.perf_counter()
    find_primes(3, 10000)
    find_primes(10001, 20000)
    find_primes(20001, 30000)
    print(f"Время работы последовательно: {int(time.perf_counter() - start_time)}")
    start_tread = time.perf_counter()
    threads = []
    num1 = 3
    num2 = 10000
    for x in range(2):
        thr = threading.Thread(target=find_primes, args=(num1, num2))
        thr.start()
        threads.append(thr)
        num1 += 10000
        num2 += 10000

    for thr in threads:
        thr.join()
    print(f"Время работы через поток: {int(time.perf_counter() - start_tread)}")

    start_multi = time.perf_counter()
    multi = []
    mult = multiprocessing.Process(target=find_primes, args=(3, 10000))
    mult.start()
    multi.append(mult)
    mult = multiprocessing.Process(target=find_primes, args=(10001, 20000))
    mult.start()
    multi.append(mult)
    mult = multiprocessing.Process(target=find_primes, args=(20001, 30000))
    mult.start()
    multi.append(mult)

    for mult in multi:
        mult.join()
    print(f"Время работы чере multiprocess: {int(time.perf_counter() - start_multi)}")