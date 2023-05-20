password = int(input('Введите цифровой пароль: '))
key = 1234
result = password ^ key
print(f'Пароль для ввода: {result}')
