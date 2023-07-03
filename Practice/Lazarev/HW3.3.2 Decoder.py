# Программа расшифрования

secret_code = 777
password = input('Введите зашифрованный пароль: ')
result = secret_code ^ int(password)
print('Расшифрованный пароль:', result)
