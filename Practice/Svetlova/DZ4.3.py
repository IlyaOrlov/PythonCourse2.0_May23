x = ""
while True:
    x1 = input("Введите символ: ")
    if x1.lower() == "stop":
        break
    if not x1.isdigit():
        print("Предупреждение: Введен нечисловой символ.")
        continue
    x += x1

print("Формированное число:", x)