import random


def numprov(x, txt):
    while not (x := input(f"Введите {txt} значение загадываемого числа :")).isnumeric():
        None
    return int(x)


numStart = numprov("text", "минимальное")
numEnd = numprov("text", "максимальное")
numTrue = random.randint(numStart, numEnd)
# для отладки print(numTrue)
numGuess = -1
while int(numGuess) != numTrue:
    numGuess = input("Какое число вы загадали?")
    if not numGuess.isnumeric():
        print("Увы и ах, возвращайся если захочешь ещё поиграть.")
        break
    if int(numGuess) == numTrue:
        print("Поздравляю, ты угадал загаданное число!")
    elif int(numGuess) < numTrue:
        print(f"Загаданное число больше чем {numGuess}.")
    else:
        print(f"Загаданное число меньше чем {numGuess}.")
