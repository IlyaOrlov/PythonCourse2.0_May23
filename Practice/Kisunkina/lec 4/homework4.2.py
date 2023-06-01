number = input("Введите пятизначное число: ")

if len(number) == 5:
    i = 0
    while i < 5:
        print(f"{i+1} цифра равна {number[i]}")
        i += 1
else:
    print("Введена неверная длина строки, введите пятизначное число")
