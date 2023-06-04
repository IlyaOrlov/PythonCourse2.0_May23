def fun(x):
    for i in range(len(x)):
        for j in range(i):
            if x[i] == x[j]:
                return x[i]


lst1 = [2, 3, 4, 5, 3, 2]
lst2 = [7, 3, 4, 9, 1, 3]
lst3 = [5, 7, 4, 8, 4, 7]
print(fun(lst1))
print(fun(lst2))
print(fun(lst3))
