x = input('Введите длину прямоугольника: ').replace(',', '.')
y = input('Введите ширину прямоугольника: ').replace(',', '.')

if x.replace('.', '').isdigit() and y.replace('.', '').isdigit():
    x_float = float(x)
    y_float = float(y)
    if x_float != 0 and y_float != 0:
        perimetr = 2 * (float(x) + float(y))
        print(f'Периметр прямоугольника = {perimetr}')
    else:
        print('Введенные значения некорректны, попробуйте еще раз')
else:
    print('Введенные значения некорректны, попробуйте еще раз')

