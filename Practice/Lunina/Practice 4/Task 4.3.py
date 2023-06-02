n = ""
while (i := input("Введите число: ")).lower() != "stop":
    if i.isdigit():
        print(f" Число: {i}")
    else:
        print("Ошибка! Введите только число ")
        continue
    n += i

print(f"Вы ввели {n}. До встречи.")
