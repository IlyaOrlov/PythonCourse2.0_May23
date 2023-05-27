def enter_int():
    while not (x := input("Введите число: ")).isdecimal():
        pass
    return int(x)


width = enter_int()
length = enter_int()
p = 2 * (width + length)
print(p)
