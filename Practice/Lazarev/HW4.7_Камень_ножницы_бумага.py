import random

z = ['камень', 'ножницы', 'бумага']
print('You wanna play??? Lets play!!!\nЧтобы начать напишите Камень, Ножницы или Бумага'
      '\nКамень бьёт ножницы, бумага оборачивает камень, ножницы режут бумагу.')
user = (input('')).lower()
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
