code = int(input("Введите комбинацию цифр: "))
key = int(input("Введите секретный код: "))
rez = code ^ key
print(f"Ваш пароль: {rez}")
