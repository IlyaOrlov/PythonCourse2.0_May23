n = 0
s = ('Ты сам-то понял, что написал?!', 'Аргументируй', 'И?!')
while (x := input('Введите слово: ')).lower() != 'хватит':
    print(s[n % 3])
    n += 1
else:
    print('Завершено')
