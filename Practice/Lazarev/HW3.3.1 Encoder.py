# Программа шифрования

secret_code = '777'
password = input('Введите пароль: ')
result = int(secret_code) ^ int(password)
print('Зашифрованный пароль: ', result)
