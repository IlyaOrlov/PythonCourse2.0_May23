while (i := input("Введите число: ")) != "stop":
    if i.isdigit():
        print(f" Число: {i}")
    else:
        print("Ошибка! Введите только число ")
        continue
print("До встречи")