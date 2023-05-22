x = input('Введите пройденное расстояние в километрах: ').replace(',', '.')
y = input('Введите время пути в часах: ').replace(',', '.')

if x.replace('.', '').isnumeric() and y.replace('.', '').isnumeric():
    x_float = float(x)
    y_float = float(y)
    if x_float >= 0 and y_float > 0:
        speed = x_float/y_float
        print(f'Средняя скорость = {speed} км/ч')
    else:
        print('Введенные значения некорректны, попробуйте еще раз')
        exit()
else:
    print('Введенные значения некорректны, попробуйте еще раз')
    exit()
