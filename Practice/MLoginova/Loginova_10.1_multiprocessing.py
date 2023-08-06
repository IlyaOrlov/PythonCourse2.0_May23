import multiprocessing
import time


def find_primes(start=3, end=None):
    pr_chisla = []
    while start <= end:
        k = 2
        while k <= start**0.5:
            if start % k == 0:
                break
            k += 1
        else:
            pr_chisla.append(start)
        start += 1
    #  print(pr_chisla)


if __name__ == "__main__":
    data = [(3, 10000), (10001, 20000), (20001, 30000)]
    start = time.perf_counter()
    lst = []
    for i in range(len(data)):
        pr = multiprocessing.Process(target=find_primes, args=data[i])
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
#  1.Время вычислений c использованием процессов в секундах: 0.07713819993659854
#  2.Время вычислений c использованием процессов в секундах: 0.08733649994246662
#  3.Время вычислений c использованием процессов в секундах: 0.09783909993711859
