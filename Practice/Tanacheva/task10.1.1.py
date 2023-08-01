import time
from math import sqrt


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


start_time = time.perf_counter()

find_primes(3, 10000)
find_primes(10001, 20000)
find_primes(20001, 30000)
end_time = time.perf_counter() - start_time
print(f"Затраченное время {end_time}")
