import random


print('Давайте сыграем в игру "Камень, ножницы, бумага!"')
answers = ['камень', 'ножницы', 'бумага']
option1 = 'бумагакамень'
option2 = 'каменьножницы'
option3 = 'ножницыбумага'
while input('Хотите сыграть? Введите: Да или Нет ').lower() != 'нет':
    you = input('Введите камень, ножницы, либо бумага: ').lower()
    if you == 'камень' or you == 'ножницы' or you == 'бумага':
        opponent = random.choice(answers)
        res = you + opponent
        print(f'Ответ оппонета: {opponent}')    # оставил для проверки
        print(f'Что получилось: {res}')         # оставил для проверки
        if you == opponent:
            print('Ничья!')
        elif res == option1 or res == option2 or res == option3:
            print('Поздравляю! Вы победили!')
        else:
            print('Жаль, но Вы проиграли!')
    else:
        print('Вы ошиблись в вводе! Попробуйте снова!')
print('Спасибо за игру! Возвращайтесь еще!')
