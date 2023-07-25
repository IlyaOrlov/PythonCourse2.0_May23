s = ""
while (symbol := input('Введите числовой символ, если хотите закончить, введите слово stop:')).lower() != "stop":
    if symbol.isdecimal():
        s += symbol
    else:
        print("Вы ввели не числовой символ, введите новый символ")
print(f"Итоговое число: {s}")
