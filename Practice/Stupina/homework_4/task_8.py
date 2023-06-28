import random


print('Игра "камень,ножницы, бумага" \n')

var = ['камень', 'ножницы', 'бумага']
while (pl_1 := input('Введите: камень, ножицы или бумага, чтобы начать игру; либо стоп - чтобы завершить:').lower()) \
       != 'стоп':
    if pl_1 not in var:
        print('Некорректный ввод, попробуйте еще раз')
        continue
    pl_2 = random.choice(var)
    if pl_1 == pl_2:
        res = 'Ничья!'
    elif (pl_1 == var[0] and pl_2 == var[1]) or (pl_1 == var[1] and pl_2 == var[2]) \
          or (pl_1 == var[2] and pl_2 == var[0]):
        res = 'Вы выиграли!'
    else:
        res = 'Вы проиграли!'
    print(f'Вы: {pl_1} \n Я: {pl_2} \n {res} \n')
