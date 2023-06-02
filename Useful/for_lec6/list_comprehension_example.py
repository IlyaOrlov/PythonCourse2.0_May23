s = "abcd24m5l3"
lst = []
for i in s:
    if i.isdecimal():
        lst.append(i)
    else:
        lst.append('*')
print(lst)

lst1 = [i if i.isdecimal() else '*' for i in s]
print(lst1)


a = 10
b = 20
if a > b:
    print(a)
else:
    print(b)

print(a if a > b else b)



