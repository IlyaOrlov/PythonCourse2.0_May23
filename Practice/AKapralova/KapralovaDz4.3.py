print("Вводите символы, чтобы получить желаемое число. Если хотите выйти из программы, напишите Stop")
a = ""
while (b := input("Введите числовой символ: ")).upper() != "STOP":
    if not b.isdecimal():
        print("Вы ввели не число: ")
    else:
        a += b
else:
    print(a)
