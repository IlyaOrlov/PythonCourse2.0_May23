n = 0
s = ('Ты сам-то понял, что написал?!', 'Аргументируй', 'И?!')
while (x := input('Введите слово: ')).lower() != 'хватит':
    n += 1
    if n % 3 == 1:
        print(s[0])
    elif n % 3 == 2:
        print(s[1])
    else:
        print(s[2])
else:
    print('Завершено')
