out = ''
while (x := input('Введите число:')).lower() != 'stop':
    if not x.isnumeric():
        print('Вы ввели нечисловой символ')
    else:
        out += x
        print(out)
else:
    print(f'Ваше итоговое число: {out}')
