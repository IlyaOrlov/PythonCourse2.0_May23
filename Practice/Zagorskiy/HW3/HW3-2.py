# Написать программу для расчёта средней скорости автомобиля по введённым значениям
# времени и расстояния, пройденного за это время.
a = int(input('Введите время в пути в часах: '))
b = int(input('Введите пройденное расстояние в километрах: '))
s = b // a
print(f'Средняя скорость автомобиля: {s} км/ч')