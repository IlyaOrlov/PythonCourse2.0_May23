def myenumerate(lst):
    i = 0
    while i < len(lst):
        yield i, lst[i]
        i += 1


lst = [1, 2, 3, 4, 5]
res = myenumerate(lst)
print(res)
for i in myenumerate(lst):
    print(i)
