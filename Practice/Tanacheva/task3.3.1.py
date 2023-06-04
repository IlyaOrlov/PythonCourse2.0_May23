password = int(input("Введите цифровой пароль: "))
key = int(input("Введите секретный код: "))

new_password = password ^ key
print(f"Зашифрованный пароль: {new_password}")
