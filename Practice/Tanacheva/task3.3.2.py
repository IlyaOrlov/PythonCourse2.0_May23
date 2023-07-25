new_password = int(input("Введите зашифрованный пароль: "))
key = int(input("Введите секретный код: "))

old_password = new_password ^ key
print(f"Пароль был расшифрован: {old_password}")
