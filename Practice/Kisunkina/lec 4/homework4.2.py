number = input("Введите пятизначное число: ")

if len(number) == 5:
        print('Первая цифра равна', number[0])
        print('Вторая цифра равна', number[1])
        print('Третья цифра равна', number[2])
        print('Четвёртая цифра равна', number[3])
        print('Пятая цифра равна', number[4])
else: print("Введена неверная длина строки, введите пятизначное число")
