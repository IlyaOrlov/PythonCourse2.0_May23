print("Эта программа должна вывести на экран большее из двух введённых чисел с помощью двух функций")
def fun1(num1, num2):
    if num2 < num1:
        print(f"Первая функция. Вывожу на экран большее число: {num1}")
    elif num1 < num2:
        print(f"Первая функция. Вывожу на экран большее число: {num2}")

def fun2(num1, num2):
    if num1 > num2:
        x = num1
    elif num2 > num1:
        x = num2
    return x

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
x = fun2(num1, num2)
fun1(num1, num2)
fun2(num1, num2)
print(f"Вторая функция. Большее число: {x}")
