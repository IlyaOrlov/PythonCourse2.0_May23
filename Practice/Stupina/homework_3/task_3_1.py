password = input('Введите цифровой пароль: ')
key = input('Введите код: ')

if password.isnumeric() and key.isnumeric():
    result = int(password) ^ int(key)
    print(f'Зашифрованный пароль: {result}')
else:
    print('Ошибка: введенный пароль/код не является цифровым')
