import random


a = int(input("Задайте начало диапазона: "))
#a = int(a)
b = int(input("Задайте конец диапазона: "))
#b = int(b)
number = random.randint(a, b)
while (guess := int(input('Введите целое число : '))) != number:
    if guess < number:
        print('Нет, загаданное число немного больше этого.')
    elif guess > number:
        print('Нет, загаданное число немного меньше этого.')

else:
    print('Поздравляю, вы угадали. Завершено')
