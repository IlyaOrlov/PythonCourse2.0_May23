a = int(input('Введите цифровой пароль: '))
key = int(input('Введите код для расшифровки: '))
result = a ^ key
print(f'Зашифрованный пароль: {result}')