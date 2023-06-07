import random


print('Давайте сыграем в игру "Камень, ножницы, бумага!"')
answers = [4, 6, 8]                            # 4-камень, 6-ножницы, 8-бумага
while input('Хотите сыграть? Введите: Да или Нет ').lower() != 'нет':
    you = input('Введите цифру 0 - камень, 1 - ножницы, либо 2 - бумага: ')
    if you in ('0', '1', '2'):
        opponent = random.choice(answers)
        res = int(you) + opponent
        print(f'Ответ оппонета: {opponent}')    # оставил для проверки
        print(f'Что получилось: {res}')         # оставил для проверки
        if res in (4, 7, 10):
            print('Ничья!')
        elif res in (6, 9):
            print('Поздравляю! Вы победили!')
        else:
            print('Жаль, но Вы проиграли!')
    else:
        print('Вы ошиблись в вводе! Попробуйте снова!')
print('Спасибо за игру! Возвращайтесь еще!')