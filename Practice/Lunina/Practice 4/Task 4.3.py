n = ""
while (i := input("Введите число: ")).lower() != "stop":
    if i.isdigit():
        print(f" Число: {i}")
        n += i
    else:
        print("Ошибка! Введите только число ")

print(f"Вы ввели {n}. До встречи.")
