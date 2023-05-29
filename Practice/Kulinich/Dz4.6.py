def myfun1(x,y):
    if x > y:
        print(x)
    else:
        print(y)


def myfun2(x,y):
    if x > y:
        return x
    else:
        return y


a = int(input("Введите 1ое число   "))
b = int(input("Введите 2ое число   "))
myfun1(a,b)
z = myfun2(a,b)
print(z)


