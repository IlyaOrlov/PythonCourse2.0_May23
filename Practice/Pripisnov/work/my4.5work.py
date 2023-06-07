import random

def secret_number():


    a = int(input("Введите начало диапазона: "))
    b = int(input("Введите конец диапазона: "))
    x = random.randint(a, b)
    y = False
    while not y:
        try:
            guess = int(input("Введите ваше число: "))
            if guess == x:
                print("Поздравляю! Вы угадали число.")
                y = True
            elif guess < x:
                print("Загаданное число больше.")
            else:
                print("Загаданное число меньше.")
        except ValueError:
            print("Некорректный ввод. Введите целое число.")
secret_number()
