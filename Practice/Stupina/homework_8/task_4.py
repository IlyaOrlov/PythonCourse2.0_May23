import itertools


# задание 1
lst_1 = list(itertools.chain([1, 2, 3], [4, 5], [6, 7]))
print(lst_1)

# задание 2
lst_in = ['hello', 'i', 'write', 'cool', 'code']
lst_2 = list(itertools.filterfalse(lambda x: len(x) < 5, lst_in))
print(lst_2)

# задание 3
lst_3 = list(itertools.combinations('password', 4))
print(lst_3)
