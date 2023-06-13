x = input('Введите запрос: ')
out = ['Ты сам-то понял, что написал?', 'Аргументируй', 'И?']
i = 0

while x.lower() != 'хватит':
    print(out[i])
    x = input('Ваш ответ: ')
    if i == len(out)-1:
        i = 0
    else:
        i += 1
