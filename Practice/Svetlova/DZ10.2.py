 # Реализовать запуск функции, осуществляющей операцию сложения для различных типов (integer, string, list) параллельно с различными наборами аргументов.

import multiprocessing

def add_elements(elements, result_queue):
    result = elements[0]
    for elem in elements[1:]:
        result += elem
    result_queue.put(result)

def parallel_addition(*args):
    processes = []
    result_queue = multiprocessing.Queue()

    for arg in args:
        p = multiprocessing.Process(target=add_elements, args=(arg, result_queue))
        processes.append(p)

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    results = []
    while not result_queue.empty():
        results.append(result_queue.get())

    return results

if __name__ == '__main__':
    # Примеры вызова функции
    integer_result = parallel_addition([1, 2, 3])
    print("Integer result:", integer_result)

    string_result = parallel_addition(["Hello, ", "world", "!"])
    print("String result:", string_result)

    list_result = parallel_addition([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print("List result:", list_result)