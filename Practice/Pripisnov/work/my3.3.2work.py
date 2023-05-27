has = int(input('Введите полученный пароль :'))
key = int(input('Введите ключ пароля :'))
res = has ^ key
print(f'Раскодированный пароль : {res}')
