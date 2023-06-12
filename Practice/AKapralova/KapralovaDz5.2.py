def repeat(x):
    s = set()
    for i in x:
        if i in s:
            return i
        s.add(i)


lst = [2, 3, 4, 5, 3, 2]
print(repeat(lst))
