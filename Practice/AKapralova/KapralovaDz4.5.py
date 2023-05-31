import random


number = random.randint(0,10)
print("Я загадала число от 0 до 10. Попробуй отгадать!")
answer = int(input("Введите целое число : "))

while answer != number:
    if answer < number:
        print("Нет, загаданное число немного больше этого. Попробуй еще раз!")
    elif answer > number:
        print("Нет, загаданное число немного меньше этого. Попробуй еще раз!")

    answer = int(input("Введите целое число : "))
else:
    print("Поздравляю, вы угадали!")
