import itertools


def merge(lst1, lst2, lst3):
    return list(itertools.chain(lst1, lst2, lst3))


# задание 1
l1 = [1, 2, 3]
l2 = [4, 5]
l3 = [6, 7]
print(merge(l1, l2, l3))


# задание 2
def filter_five(mas1):
    return list(itertools.filterfalse(lambda i: len(i) < 5, mas1))


mas = (['hello', 'i', 'write', 'cool', 'code'])
print(filter_five(mas))


# задание 3
def combinations_four(stroka):
    for item in itertools.combinations(stroka, 4):
        yield item


s = combinations_four("password")
for ii in s:
    print(ii)
