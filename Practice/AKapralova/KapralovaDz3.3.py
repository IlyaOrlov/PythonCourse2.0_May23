password = int(input("Введите цифровой пароль: "))
key = int(input("Введите код: "))
result = password ^ key
print(f"Зашифрованый пароль: {result}")

result = int(input("Введите зашифрованый пароль: "))
key = int(input("Введите код: "))
unpassword = result ^ key
print(f"Расшифрованый пароль: {unpassword}")
