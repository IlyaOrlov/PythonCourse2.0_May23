# программа для шифровки кода

password = int(input('Введите цифровой пароль: '))
key = 1805
result = password ^ key
print(f'Зашифрованный пароль: {result}')

# программа для расшифровки кода

anpassword = result ^ key
print(f'Расшифрованный пароль: {anpassword}')
