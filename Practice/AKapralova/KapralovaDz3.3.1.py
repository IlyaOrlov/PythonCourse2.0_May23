print("Программа для шифрования кода.")
password = int(input("Введите цифровой пароль: "))
key = int(input("Введите код: "))
result = password ^ key
print(f"Зашифрованый пароль: {result}")
