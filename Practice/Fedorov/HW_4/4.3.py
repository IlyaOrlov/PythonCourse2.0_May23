num = ""
while not (x := input("Введите числовые символы: ")).lower() == "stop":
    if not x.isnumeric():
        print("Ошибка! Нужно вводить цифры.")
        x = ""
    num += x
print(f"Вы ввели : {num}")
