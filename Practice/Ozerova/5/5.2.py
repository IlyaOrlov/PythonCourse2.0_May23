def dubl(x):
    y = set()
    for i in x:
        if i in y:
            return i
        y.add(i)


lst = [2, 3, 4, 5, 3, 2]
print(dubl(lst))