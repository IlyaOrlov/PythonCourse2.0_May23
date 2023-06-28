from itertools import *


# задание 1
lst_1 = []
for i in chain([1, 2, 3], [4, 5], [6, 7]):
    lst_1.append(i)
print(lst_1)

# задание 2
lst_in = ['hello', 'i', 'write', 'cool', 'code']
lst_2 = []
for i in filterfalse(lambda x: len(x) < 5, lst_in):
    lst_2.append(i)
print(lst_2)

# задание 3
for i in permutations('password', 4):  # возможно я неправильно поняла,что нужно вывести
    print(i)
