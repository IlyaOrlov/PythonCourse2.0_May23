import random

print('You wanna play??? Lets play!!!\nЧтобы начать напишите Камень, Ножницы или Бумага'
          '\nКамень бьёт ножницы, бумага оборачивает камень, ножницы режут бумагу.')
z = ('камень', 'ножницы', 'бумага')
while True:
    user = input('').lower()
    bot = random.choice(z)
    print(f'Компьютер вбрал: {bot}')
    if user == bot:
        print('Ничья!')
    elif user == 'камень':
        if bot == 'ножницы':
            print('Вы победили!')
        else:
            print('Вы проиграли!')
    elif user == 'бумага':
        if bot == 'камень':
            print('Вы победили!')
        else:
            print('Вы проиграли!')
    elif user == 'ножницы':
        if bot == 'бумага':
            print('Вы победили!')
        else:
            print('Вы проиграли!')

    play_again = ''
    play_again = input('Сыграем еще? (да/нет): ')
    if play_again.lower() != 'да':
        break
    else:
        print('Напишите Камень, Ножницы или Бумага')
