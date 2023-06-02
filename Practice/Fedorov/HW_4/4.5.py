import random


def numprov(x, txt):
    while not (x := input(f"Введите {txt} значение загадываемого числа :")).isnumeric():
        pass
    return int(x)


num_start = numprov("text", "минимальное")
num_end = numprov("text", "максимальное")
num_true = random.randint(num_start, num_end)
# для отладки print(numTrue)
num_guess = -1
while int(num_guess) != num_true:
    num_guess = input("Какое число вы загадали?")
    if not num_guess.isnumeric():
        print("Увы и ах, возвращайся если захочешь ещё поиграть.")
        break
    i_num_guess = int(num_guess)
    if i_num_guess == num_true:
        print("Поздравляю, ты угадал загаданное число!")
    elif i_num_guess < num_true:
        print(f"Загаданное число больше чем {num_guess}.")
    else:
        print(f"Загаданное число меньше чем {num_guess}.")
