print("Программа для расшифровки кода.")
result = int(input("Введите зашифрованый пароль: "))
key = int(input("Введите код: "))
unpassword = result ^ key
print(f"Расшифрованый пароль: {unpassword}")
