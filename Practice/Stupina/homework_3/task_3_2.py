password_code = input('Введите зашифрованный пароль: ')
key = input('Введите код: ')

if password_code.isnumeric() and key.isnumeric():
    result = int(password_code) ^ int(key)
    print(f'Ваш пароль: {result}')
else:
    print('Ошибка: введенный пароль/код не является цифровым')
