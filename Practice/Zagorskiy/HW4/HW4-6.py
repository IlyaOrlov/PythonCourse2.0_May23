# Написать и вызвать две функции, принимающие два числа.
# Первая функция должна вывести на экран большее из двух введённых чисел.
# Другая должна вернуть большее из двух введённых чисел по месту вызова.
def fun1(a, b):
    if a > b:
        print(f'Первая функция. Большее число: {a}')
    else:
        print(f'Первая функция. Большее число: {b}')


def fun2(a, b):
    if a > b:
        return a
    else:
        return b


print('В данной программе реализованы 2 функции, которые сравнивают 2 числа и выводят большее.')
print()
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

fun1(a, b)
x = fun2(a, b)
print(f"Вторая функция. Большее число: {x}")
