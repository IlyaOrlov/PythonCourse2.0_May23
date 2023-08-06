import itertools


# Функция, принимающая три массива и возвращающая один массив:
def merge_arrays(arr1, arr2, arr3):
    merged = itertools.chain(arr1, arr2, arr3)
    result = list(merged)
    return result


# Пример использования функции
a1 = [1, 2, 3]
a2 = [4, 5]
a3 = [6, 7]
res = merge_arrays(a1, a2, a3)
print(res)
