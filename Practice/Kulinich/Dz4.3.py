y = ""
while (i := input("Введите число  ")) != "stop":
    if not i.isnumeric():
        print("Вы ввели не число,введите число ")
    else:
        y = y + str(i)
else:
    print(y)
