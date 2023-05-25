password = int(input("Введите пароль: "))
kod = int(input("Введите секретный код: "))
print(f"Зашифрованный пароль: {password ^ kod}")
