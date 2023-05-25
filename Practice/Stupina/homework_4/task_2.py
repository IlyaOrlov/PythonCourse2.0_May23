while len(x := input('введите целое пятизначное число:')) != 5 or not x.isdecimal():
    print('Вы ввели не целое пятизначное число')
else:
    for i in range(len(x)):
        print(f'{i+1} цифра равна {x[i]}')
