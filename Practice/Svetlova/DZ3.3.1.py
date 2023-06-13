b = int(input('Введите зашифрованный пароль: '))
key = int(input('Введите код для расшифровки: '))
result = b ^ key
print(f'Расшифрованный пароль: {result}')