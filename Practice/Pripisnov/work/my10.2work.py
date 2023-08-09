import threading
import multiprocessing

def sum_integers(a, b):
    return a + b

def concatenate_strings(a, b):
    return a + b

def concatenate_lists(a, b):
    return a + b

def parallel_sum(function, args_list):
    results = []
    threads = []

    for args in args_list:
        thread = threading.Thread(target=results.append, args=(function(*args),))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return results


# Пример использования функции parallel_sum
integer_args = [(1, 2), (3, 4), (5, 6)]
string_args = [('Hello', ' World'), ('Parallel', ' Processing'), ('Python', ' Multithreading')]
list_args = [([1, 2, 3], [4, 5, 6]), ([7, 8], [9, 10]), ([11, 12], [13, 14, 15])]

# Выполнение сложения для различных типов данных параллельно
results_integers = parallel_sum(sum_integers, integer_args)
results_strings = parallel_sum(concatenate_strings, string_args)
results_lists = parallel_sum(concatenate_lists, list_args)

print("Результаты сложения для integer:")
print(results_integers)

print("Результаты сложения для string:")
print(results_strings)

print("Результаты сложения для list:")
print(results_lists)
