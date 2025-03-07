import threading
import time
import Loginova_10

if __name__ == "__main__":
    data = [(3, 10000), (10001, 20000), (20001, 30000)]
    start = time.perf_counter()
    threads = []
    for i in range(len(data)):
        thr = threading.Thread(target=Loginova_10.find_primes, args=(*data[i],))
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
#  Время вычислений c использованием потоков в секундах: 0.031701300060376525

