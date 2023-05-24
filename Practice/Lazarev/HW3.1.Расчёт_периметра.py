# Расчёт периметра
length = float(input('Введите длину (в см): '))
width = float(input('Введите ширину (в см): '))
perimeter = (length + width) * 2
if length != width:
    print('Периметр прямоугольника =', perimeter ,'см')
elif length == width:
    print('Периметр квадрата =', perimeter ,'см')

