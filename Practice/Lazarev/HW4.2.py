a = 1
while (s := input('Введите пятитизначное число: ')):
    if not s.isdigit():
        print('Вы ввели не цифры!')
    elif len(s) != 5:
        print('Число должно быть пятизначным!')
    else:
        print(f'Число: {s}')
        for i in s:
            a += 1
            print(f'{a} цифра равна {i}')
            
