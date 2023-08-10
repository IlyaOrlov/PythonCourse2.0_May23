# программа для расшифровки пароля

anpassword = int(input('Введите получившийся пароль для расшифровки: '))
key = 1805
result = anpassword ^ key
print(f'Расшифрованный пароль: {result}')
