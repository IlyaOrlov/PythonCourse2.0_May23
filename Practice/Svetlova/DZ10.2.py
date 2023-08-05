 # Реализовать запуск функции, осуществляющей операцию сложения для различных типов (integer, string, list) параллельно с различными наборами аргументов.

import threading


def parallel_addition(*args):
    results = []

    def add_elements(elements):
        result = elements[0]
        for elem in elements[1:]:
            result += elem
        results.append(result)

    threads = []
    t = threading.Thread(target=add_elements, args=(args,))
    threads.append(t)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    return results


# Примеры вызова функции
integer_result = parallel_addition(1, 2, 3)
print("Integer result:", integer_result)

string_result = parallel_addition("Hello, ", "world", "!")
print("String result:", string_result)

list_result = parallel_addition([1, 2, 3], [4, 5, 6], [7, 8, 9])
print("List result:", list_result)
