code = int(input('Введите секретный код: '))
key = 1234
result = code ^ key
print(f'Цифровой пароль: {result}')
