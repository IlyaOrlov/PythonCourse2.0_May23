import itertools


# Функция, принимающая массив строк и возвращающая только строки с длиной не меньше пяти:
def filter_strings(strings):
    filtered = itertools.filterfalse(lambda x: len(x) < 5, strings)
    result = list(filtered)
    return result


# Пример использования функции
s = ['hello', 'i', 'write', 'cool', 'code']
res = filter_strings(s)
print(res)
