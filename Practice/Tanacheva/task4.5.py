import random


min1 = int(input("Введите нижнюю границу для чисел:"))
max1 = int(input("Введите вверхнюю границу для чисел:"))
number1 = random.randint(min1, max1)
# print(number1)
print("")
print("Угадай число!")

while (number2 := input('Введите число:')).isdigit():
    if int(number2) > number1:
        print("Введенное число больше загаданного")
    elif int(number2) < number1:
        print("Введенное число меньше загаданного")
    elif int(number2) == number1:
        print("Вы угадали число")
        break
