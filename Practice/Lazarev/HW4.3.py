print('Вводите цифры, чтобы получить число.\nЧтобы получить результат напишите Stop.')
##r = 0
r = ''
while (s := input('Вводите цифры: ').lower()) != 'stop':
    if not s.isdecimal: #почему не работает со строкой - не понимаю
        print('Вы ввели не цифры!')
    else:
        r += s
##        r = r * 10 + int(s) 
print(f'Число равно:', r)
