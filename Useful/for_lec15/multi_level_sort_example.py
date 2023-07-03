from functools import cmp_to_key

# d = {3: 'b', 1: 'a', 2: 'b', 4: 'c'}
# print([s for s in d.items()])
# sorted_d = sorted(d.items(), key=lambda pair: pair[1])
# print(sorted_d)

# lst = [(1, 2, 3), (3, 4, 5), (2, 2, 5)]
# sorted_lst = sorted(lst)
# print(sorted_lst)
# sorted_lst1 = sorted(lst, key=lambda t: (t[1], -t[0], t[2]))
# print(sorted_lst1)


class MyCmp:
    def __init__(self, elem, cmp_fun):
        self.elem = elem
        self.cmp_fun = cmp_fun

    def __lt__(self, other):
        return self.cmp_fun(self.elem, other.elem)


def cmp_fun(x, y):
    def diff(a, b):
        if a > b:
            return 1
        elif a < b:
            return -1
        else:
            return 0

    if x[1] == y[1]:
        if x[0] == y[0]:
            return diff(x[2], y[2])
        else:
            return diff(x[0], y[0])
    else:
        return diff(y[1], x[1])


def cmp_fun2(x, y):
    return x - y


lst = [("Ivan", "Ivanov", 1990), ("Petr", "Petrov", 1995), ("Petr", "Ivanov", 1992), ("Ivan", "Petrov", 1995)]
print(sorted(lst))
# print(sorted(lst, key=lambda t: MyCmp(t, cmp_fun)))
print(sorted(lst, key=cmp_to_key(cmp_fun)))
