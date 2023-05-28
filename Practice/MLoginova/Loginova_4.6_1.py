#функция должна вывести на экран большее из двух введённых чисел без места требования
def myfun1(x, y):
    if int(x) < int(y):
        print(y)
        return y
    else:
        print(x)
        return x


myfun1(3, 20)
