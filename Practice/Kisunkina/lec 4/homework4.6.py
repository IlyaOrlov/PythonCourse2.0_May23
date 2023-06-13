def fun1(num1, num2):
    if num2 < num1:
        print(f"Первая функция. Вывожу на экран большее число: {num1}")
    elif num1 < num2:
        print(f"Первая функция. Вывожу на экран большее число: {num2}")
    else:
        print("Значения равны между собой - я не могу вывести большее")


def fun2(number_1, number2):
    x = None
    if number_1 > number2:
        x = number_1
    elif number2 > number_1:
        x = number2
    else:
        print("Значения равны между собой - я не могу вывести большее")
    return x

print("Эта программа должна вывести на экран большее из двух введённых чисел с помощью двух функций")
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
fun1(num1, num2)
fun2(num1, num2)

