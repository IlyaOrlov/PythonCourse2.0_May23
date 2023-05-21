# программа для шифровки пароля

password = int(input('Введите цифровой пароль: '))
key = 1805
result = password ^ key
print(f'Зашифрованный пароль: {result}')
