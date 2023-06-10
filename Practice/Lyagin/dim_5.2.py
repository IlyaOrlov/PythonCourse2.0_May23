def povtor(lst):
    for i in range(len(lst)):
        for k in range(i):
            if lst[i] == lst[k]:
                return (lst[i])


lst = [2, 3, 4, 5, 3, 2]
print(povtor(lst))
