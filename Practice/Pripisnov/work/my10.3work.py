import threading

# Создаем объект Thread-local storage для каждого потока
thread_local_data = threading.local()

def print_private_data():
    # Получаем имя исполняемого потока
    thread_name = threading.current_thread().name

    # Проверяем, есть ли у потока приватные данные
    if not hasattr(thread_local_data, 'private_data'):
        thread_local_data.private_data = "Private data for " + thread_name

    # Выводим имя потока и его приватные данные
    print(thread_name + ": " + thread_local_data.private_data)

def run_threads():
    # Создаем и запускаем несколько потоков
    threads = []
    for i in range(5):
        thread = threading.Thread(target=print_private_data)
        threads.append(thread)
        thread.start()

    # Дожидаемся завершения всех потоков
    for thread in threads:
        thread.join()

run_threads()
