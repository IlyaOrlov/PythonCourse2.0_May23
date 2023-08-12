import itertools


# Задание 1
def combiner(x1, y1, z1):
    return list(itertools.chain(x1, y1, z1))


lst1 = [1, 2, 3]
lst2 = [4, 5]
lst3 = [6, 7]
print(combiner(lst1, lst2, lst3))


# Задание 2
def filter_mas(x2):
    return list(itertools.filterfalse(lambda s: len(s) < 5, x2))


lst4 = ['hello', 'i', 'write', 'cool', 'code']
print(filter_mas(lst4))


# Задание 3
def combinations(x3, y3):
    return list(itertools.combinations(x3, y3))


word = 'password'
length = 4
res = combinations(word, length)
for i in res:
    print(i)
