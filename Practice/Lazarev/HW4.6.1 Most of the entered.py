def first_func(a, b):
    if a > b:
        return f'Большее число: {a}'
    else:
        return f'Большее число: {b}'


a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
print(first_func())
