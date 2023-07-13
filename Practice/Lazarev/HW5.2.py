def fun(x):
    for i in range(len(x)):
        for j in range(i):
            if x[i] == x[j]:
                return x[i]


lst1 = [2, 3, 4, 5, 3, 2]
print(fun(lst1))