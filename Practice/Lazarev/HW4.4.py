a1 = 'Ты сам-то понял, что написал?'
a2 = 'Аргументируй!'
a3 = 'И?'
i = 0
while (user := input('Напишите что-нибудь: ').lower()) != 'хватит':
    i += 1
    if i % 3 == 1:
        print(a1)
    elif i % 3 == 0:
        print(a3)
    else:
        print(a2)