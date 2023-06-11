print('Вводите цифры, чтобы получить число.\nЧтобы получить результат напишите Stop.')
r = 0
while True(s := input('Вводите цифры: ')
##    s = input('Вводите цифры: ')
##    s = s.lower()
    if s == 'stop':
        break
    elif not s.isdigit():
        print('Вы ввели не цифры!')
    else:
        r = r * 10 + int(s) 
print(f'Число равно: {r}')
