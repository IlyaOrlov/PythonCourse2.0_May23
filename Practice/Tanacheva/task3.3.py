password = int(input("Введите цифровой пароль: "))
key = int(input("Введите секретный код: "))

new_password = password ^ key
print(f"Зашифрованный пароль: {new_password}")

old_password = new_password ^ key
print(f"Пароль был расшифрован: {old_password}")
