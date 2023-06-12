def repeat(x):
    lst1 = set()
    for i in lst:
        if i in lst1:
            return i
        lst1.add(i)


lst = [2, 3, 4, 5, 3, 2]
print(repeat(lst))
