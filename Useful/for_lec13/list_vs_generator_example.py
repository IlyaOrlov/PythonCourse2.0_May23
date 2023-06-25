lst = [1, 2, 3, 4, 5]

a = [x ** 2 for x in lst]
print(a)

b = (x ** 2 for x in lst)
print(b)
for i in b:
    print(i)
