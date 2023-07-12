def fun(n, m):
    i = n
    lst = []
    while len(lst) < m:
        if i % 2 == 0:
            lst.append(i)
        i += 1
    return lst


f = fun(2, 1000000)
print(f)

