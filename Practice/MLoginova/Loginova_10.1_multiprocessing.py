import multiprocessing
import time
import Loginova_10


if __name__ == "__main__":

    data = [(3, 10000), (10001, 20000), (20001, 30000)]
    start = time.perf_counter()
    lst = []
    for i in range(len(data)):
        pr = multiprocessing.Process(target=Loginova_10.find_primes, args=data[i])
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
#  Время вычислений c использованием процессов в секундах: 0.03076120000332594
