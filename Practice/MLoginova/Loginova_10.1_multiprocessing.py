import multiprocessing
import time


def find_primes(start=3, end=None):
    pr_chisla = []
    for i in range(start, end + 1):
        for j in range(start, i + 1):
            if i % j == 0:
                break
        else:
            pr_chisla.append(i)


if __name__ == "__main__":
    data = [(3, 10000), (10001, 20000), (20001, 30000)]
    start = time.perf_counter()
    lst = []
    for k in range(len(data)):
        pr = multiprocessing.Process(target=find_primes, args=data[k])
        pr.start()
        # Если забыть выполнить start для процессов, то аналогично потокам, мы не направим ОС команду на создание
        # процесса
        # код вернёт исключение AssertionError: can only join a started process
        # дословно может присоединиться только к запущенному процессу
        lst.append(pr)
    for pr in lst:
        pr.join()
        #  Если забыть выполнить join для процессов, то программа завершит свое выполнение, не дожидаясь завершения
        #  наших процессов
        print(f'Время вычислений c использованием процессов в секундах: {time.perf_counter() - start}')
#   Время вычислений c использованием процессов в секундах: 0.287327199941501
#   Время вычислений c использованием процессов в секундах: 1.6711924000410363
#  Время вычислений c использованием процессов в секундах: 1.671219200012274
