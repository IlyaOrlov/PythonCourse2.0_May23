import itertools


lst1 = itertools.chain([1, 2, 3], [4, 5], [6,7])
print(list(lst1))

lst2 = ['hello', 'i', 'write', 'cool', 'code']
res = list(itertools.filterfalse(lambda x: len(x) < 5, lst2))
print(res)

lst3 = itertools.combinations('password', 4)
print(list(lst3))
