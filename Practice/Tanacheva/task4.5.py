import random


min1 = int(input("Введите нижнюю границу для чисел:"))
max1 = int(input("Введите вверхнюю границу для чисел:"))
number1 = random.randint(min1, max1)
# print(number1)
print("")
print("Угадай число!")

while (number2 := input('Введите число:')).isdigit():
    number2 = int(number2)
    if number2 > number1:
        print("Введенное число больше загаданного")
    elif number2 < number1:
        print("Введенное число меньше загаданного")
    else:
        print("Вы угадали число")
        break
