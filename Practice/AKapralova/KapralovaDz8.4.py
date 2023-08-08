import itertools


lst1 = list(itertools.chain([1, 2, 3], [4, 5], [6, 7]))
print(lst1)

lst = ['hello', 'i', 'write', 'cool', 'code']
lst2 = list(itertools.filterfalse(lambda x: len(x) < 5, lst))
print(lst2)

lst3 = list(itertools.combinations('password', 4))
print(lst3)
