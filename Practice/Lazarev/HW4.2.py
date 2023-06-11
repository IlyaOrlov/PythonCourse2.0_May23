##a = 1
while (s := input('Введите пятитизначное число: ')):
    if not s.isdigit():
        print('Вы ввели не цифры!')
    elif len(s) != 5:
        print('Число должно быть пятизначным!')
    else:
        a = 1
        print(f'Число: {s}')
        for i in s:
            print(f'{a} цифра равна {i}')
            a += 1
        
