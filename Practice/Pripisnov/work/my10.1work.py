def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes(start=3, end=100):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes


import time

# Запуск три раза последовательно
for i in range(3):
    start_time = time.time()
    primes = find_primes(3, 10000)
    end_time = time.time()
    print(f"Простые числа от 3 до 10000 найдены за {end_time - start_time} секунд.")


import multiprocessing

# Запуск три раза в отдельных процессах
processes = []
for i in range(3):
    process = multiprocessing.Process(target=find_primes, args=(20001 + i * 10000, 30000 + i * 10000))
    processes.append(process)
    process.start()
    # process.join() - НЕ вызываем join здесь
    for process in processes:
        process.join()
#Для тестирования важно не забывать вызывать join() для потоков и процессов после их запуска,
# чтобы дождаться их завершения. Если вы забудете выполнить join(),
# основной поток (или процесс) может завершиться раньше, чем дочерние потоки (или процессы),
# и результаты выполнения могут быть непредсказуемыми или даже ошибочными.

import timeit

# Замер времени исполнения функции find_primes для каждого диапазона
time_seq_1 = timeit.timeit(lambda: find_primes(3, 10000), number=1)
time_seq_2 = timeit.timeit(lambda: find_primes(10001, 20000), number=1)
time_seq_3 = timeit.timeit(lambda: find_primes(20001, 30000), number=1)

print(f"Время выполнения последовательного варианта 1: {time_seq_1} сек.")
print(f"Время выполнения последовательного варианта 2: {time_seq_2} сек.")
print(f"Время выполнения последовательного варианта 3: {time_seq_3} сек.")
