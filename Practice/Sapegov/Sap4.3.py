print('Вводите символы, чтобы получить желаемое число!\nЧтобы выйти из программы, введите stop')
x = ''
x1 = ''
while True:
    x = input('Введите числовой символ: ')
    x = x.lower()
    if x == 'stop':
        print(f'Ваше число: {x1}')
        print('До свидания!')
        break
    elif not x.isdigit():
        print('Вы ввели не числовой символ, пожалуйста, повторите попытку')
    else:
        x1 += x