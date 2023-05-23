num = ""
while not (x := input("Введите числовые символы: ")).lower() == "stop":
    while not x.isnumeric():
        x = input("Ошибка! Введите цифры: ")
    num += x
print(f"Вы ввели : {num}")
