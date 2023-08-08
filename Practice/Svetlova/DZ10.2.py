 # Реализовать запуск функции, осуществляющей операцию сложения для различных типов (integer, string, list) параллельно с различными наборами аргументов.

import multiprocessing

def add_elements(elements, result_queue):
    result = elements[0]
    for elem in elements[1:]:
        result += elem
    print("Sum:", result)
    result_queue.put(result)

if __name__ == '__main__':
    p1_result_queue = multiprocessing.Queue()
    p2_result_queue = multiprocessing.Queue()
    p3_result_queue = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=add_elements, args=([1, 2, 3], p1_result_queue))
    p2 = multiprocessing.Process(target=add_elements, args=(["Hello, ", "world", "!"], p2_result_queue))
    p3 = multiprocessing.Process(target=add_elements, args=([[1, 2, 3], [4, 5, 6], [7, 8, 9]], p3_result_queue))

    processes = [p1, p2, p3]

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    p1_result = p1_result_queue.get()
    p2_result = p2_result_queue.get()
    p3_result = p3_result_queue.get()


("List result:", list_result)