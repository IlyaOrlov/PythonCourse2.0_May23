answer1 = 'Ты сам-то понял, что написал?'
answer2 = 'Аргументируй'
answer3 = 'И?'
i = 0
while input('Введите утверждение: ') != 'хватит':
    i += 1
    if i % 3 == 1:
        print(answer1)
    elif i % 3 == 0:
        print(answer3)
    else:
        print(answer2)
