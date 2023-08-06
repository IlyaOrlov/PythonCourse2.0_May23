import threading
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
    threads = []
    for k in range(len(data)):
        thr = threading.Thread(target=find_primes, args=(*data[k],))
        thr.start()
        #Если забыть выполнить start для потоков, то мы не направим ОС команду на создание потока,
        # код вернёт исключение RuntimeError: cannot join thread before it is started
        #дословно невозможно присоединиться к потоку до его запуска
        threads.append(thr)
    for thr in threads:
        thr.join()
        #Если забыть выполнить join для потоков, то мы бросили наши len(data) потоков не дождавшись их объединения
        #программа завершит свое выполнение, не дожидаясь завершения наших потоков в итоге замеряемое время для каждого
        # потока будет неккоректным
        print(f'Время вычислений c использованием потоков в секундах: {time.perf_counter() - start}')
#  1.Время вычислений c использованием потоков в секундах: 0.41255850007291883
#  2.Время вычислений c использованием потоков в секундах: 3.316565199987963
#  3.Время вычислений c использованием потоков в секундах: 3.3165892000542954
