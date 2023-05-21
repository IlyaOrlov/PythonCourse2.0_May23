#расшифровка
has = input("Введите секретный код:  ")
key = 5961
result = int(has)^int(key)
print(f"Ваш пароль: {result}")
