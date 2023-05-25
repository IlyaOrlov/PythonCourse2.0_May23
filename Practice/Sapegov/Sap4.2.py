y = 1
x = input('Введите пятизначное число: ')
if not x.isdigit():
    print('Вы ввели не цифры!')
elif len(x) != 5:
    print('Число должно быть пятизначным!')
else:
    print(f'Число: {x}')
    for i in x:
        print(f'{y} цифра равна {i}')
        y += 1
