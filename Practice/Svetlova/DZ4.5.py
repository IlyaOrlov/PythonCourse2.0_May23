import random

# def guess_number():
#     x = int(input("Введите минимальное число диапазона: "))
#     y = int(input("Введите максимальное число диапазона: "))
#
#     secret_number = random.randint(x, y)
#
#     while True:
#         guess = int(input("Угадайте число: "))
#
#         if guess == secret_number:
#             print("Поздравляю! Вы угадали число.")
#             break
#         elif guess < secret_number:
#             print("Загаданное число больше.")
#         else:
#             print("Загаданное число меньше.")
#
# guess_number()


def guess_number(x, y):
    secret_number = random.randint(x, y)

    while True:
        guess = int(input("Угадайте число: "))

        if guess == secret_number:
            print("Поздравляю! Вы угадали число.")
            break
        elif guess < secret_number:
            print("Загаданное число больше.")
        else:
            print("Загаданное число меньше.")


x = int(input("Введите минимальное число диапазона: "))
y = int(input("Введите максимальное число диапазона: "))


guess_number(x, y)