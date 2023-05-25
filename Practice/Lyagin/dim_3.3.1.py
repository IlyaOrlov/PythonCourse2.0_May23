code = int(input("Введите цифровой пароль: "))
key = int(input("Введите секретный код: "))
rez = code ^ key
print(f"Отправьте другу: {rez}")
