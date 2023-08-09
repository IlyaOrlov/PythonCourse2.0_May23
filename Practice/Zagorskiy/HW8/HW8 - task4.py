# Требуется написать код, который использует указанные входные данные и выводит на экран возвращаемое значение.
# Помните, что функции могут возвращать генератор, который нужно "развернуть" для вывода на экран.
# Функция должна принимать три массива ([1, 2, 3], [4, 5], [6, 7]), а вернуть лишь один массив ([1, 2, 3, 4, 5, 6, 7])
# Функция принимает массив (['hello', 'i', 'write', 'cool', 'code']) и возвращает массив из элементов, у которых длина
# не меньше пяти (['hello', 'write’])
# Функция выдает на строку 'password' все возможные комбинации вида ([('p', 'a', 's', 's'), ('p', 'a', 's', 'w'),
# ('p', 'a', 's', 'o'), ...)
import itertools


def fun1(a, b, c):
    lst = []
    elm = itertools.chain(a, b, c)
    for i in elm:
        lst.append(i)
    return lst


def fun2(arr):
    lst = []
    for i in arr:
        if len(i) >= 5:
            lst.append(i)
    return lst


def fun3(s):
    res = []
    r = itertools.combinations_with_replacement(s, 4)
    for elm in r:
        res.append(elm)
    return res


# Задание 1
arr1 = [1, 2, 3]
arr2 = [4, 5]
arr3 = [6, 7]
j = fun1(arr1, arr2, arr3)
print(f"Результат 1 задания: функция возвращает >>> {j}")

# Задание 2
lst = ['hello', 'i', 'write', 'cool', 'code']
k = fun2(lst)
print(f"Результат 1 задания: функция возвращает >>> {k}")

# Задание 3
s = 'password'
r = fun3(s)
print(f"Результат 1 задания: функция возвращает >>> {r}")

