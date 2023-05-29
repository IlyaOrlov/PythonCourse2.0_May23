a = 1
while (s := input('Введите пятитизначное число: ')):
    if not s.isdigit():
        print('Вы ввели не цифры!')
        continue
    elif len(s) != 5:
        print('Число должно быть пятизначным!')
        continue
    else:
        print(f'Число: {s}')
        for i in s:
            print(f'{a} цифра равна {i}')
            a += 1