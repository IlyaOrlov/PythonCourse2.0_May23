import itertools


def add_lst(lst1, lst2, lst3):
    return list(itertools.chain(lst1, lst2, lst3))


def line5(lst):
    return list(itertools.filterfalse(lambda i: len(i)<5, lst))


def my_combinations(lst):
    return list(itertools.combinations(lst,4))

l1 = [1, 2, 3]
l2 = [4, 5]
l3 = [6, 7]
lst1 = ['hello', 'i', 'write', 'cool', 'code']
print(add_lst(l1, l2, l3))
print(line5(lst1))
print(my_combinations("password"))