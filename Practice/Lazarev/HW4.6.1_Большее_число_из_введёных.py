def first_func():
    while not (x := input('Введите число: ')).isdecimal():
        print('Это не число!')
    return int(x)

a = first_func()
b = first_func()
print(f'Большее число: {max(a,b)}')
