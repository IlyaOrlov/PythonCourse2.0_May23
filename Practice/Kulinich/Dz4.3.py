y = ""
while (i := input("Введите число  ").upper()) != "STOP":
    if not i.isnumeric():
        print("Вы ввели не число,введите число ")
    else:
        y += str(i)
else:
    print(y)
