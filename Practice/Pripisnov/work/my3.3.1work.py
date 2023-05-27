has = int(input('Введите числовой пароль :'))
key = int(input('Введите ключ пароля :'))
res = has ^ key

print(f'Пароль для передачи : {res}')
