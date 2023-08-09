import time
from fun_10 import find_primes


start_time = time.perf_counter()

find_primes(3, 10000)
find_primes(10001, 20000)
find_primes(20001, 30000)
end_time = time.perf_counter() - start_time
print(f"Затраченное время {end_time}")
