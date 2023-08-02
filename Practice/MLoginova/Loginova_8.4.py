import itertools

#  1
l1 = itertools.chain([1, 2, 3], [4, 5], [6, 7])
print(list(l1))
#  2
l2 = ['hello', 'i', 'write', 'cool', 'code']
res = list(itertools.filterfalse(lambda x: len(x) < 5, l2))
print(res)

#  3
l3 = itertools.combinations('password', 4)
print(list(l3))
