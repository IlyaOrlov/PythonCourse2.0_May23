import threading
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
    threads = []
    for i in range(len(data)):
        thr = threading.Thread(target=find_primes, args=(*data[i],))
        thr.start()
        # Если забыть выполнить start для потоков, то мы не направим ОС команду на создание потока,
        # код вернёт исключение RuntimeError: cannot join thread before it is started
        # дословно невозможно присоединиться к потоку до его запуска
        threads.append(thr)
    for thr in threads:
        thr.join()
        #  Если забыть выполнить join для потоков, то мы бросили наши len(data) потоков не дождавшись их объединения
        #  программа завершит свое выполнение, не дожидаясь завершения наших потоков в итоге замеряемое время
        #  для каждого потока будет неккоректным
        print(f'Время вычислений c использованием потоков в секундах: {time.perf_counter() - start}')
#  1.Время вычислений c использованием потоков в секундах: 0.05176529998425394
#  2.Время вычислений c использованием потоков в секундах: 0.08369849994778633
#  3.Время вычислений c использованием потоков в секундах: 0.10709089995361865
