# Реализовать приложение, загадывающее целое число из заданного пользователем диапазона
# и предлагающее пользователю это число угадать. Отгадывание числа должно быть реализовано
# в цикле: пока пользователь не угадает, или не введет нечисловой символ, продолжать опрос.
# Если пользователь вводит неправильное число, вывести подсказку: больше оно или меньше загаданного.
import random


print("Привет, давай сыграем! Введи диапазон чисел, а я загадаю число,\n"
      "потом ты попытаешься его угадать. Если не получится, то я дам подсказку!\n"
      "Если тебе надоест, просто напиши 'хватит'\n"
      "")

a = int(input('Введи первое число диапазона: '))
b = int(input('Введи второе число диапазона: '))
num = random.randint(a, b)
print('Я выбрал число, попробуй угадать?')

while (x := input("Угадай число: ")).upper() != "ХВАТИТ":
    if x.isdecimal():
        x = int(x)
        if x == num:
            print(f'Ты угадал! Я выбрал число {num}')
            print("Программа успешно завершена!")
            break
        elif x < num:
            print("Почти, число больше! Попробуй еще.")
        else:
            print("Почти, число меньше! Попробуй еще.")
    else:
        print('Это не число! Попробуй еще раз.')
else:
    print("Программа успешно завершена!")
