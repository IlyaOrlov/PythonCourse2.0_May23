import random

def play_game():
    print("Игра 'Камень, Ножницы, Бумага'")
    print("Выберите один из вариантов:")
    print("1 - Камень")
    print("2 - Ножницы")
    print("3 - Бумага")

    choices = ["камень", "ножницы", "бумага"]

    while True:
        your_choice = int(input("Ваш выбор (1-3): "))
        if your_choice in [1, 2, 3]:
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")

    partner_choice = random.randint(1, 3)

    print("Ваш выбор:", choices[your_choice - 1])
    print("Выбор партнёра:", choices[partner_choice - 1])

    if your_choice == partner_choice:
        print("Ничья!")
    elif (your_choice == 1 and partner_choice == 2) or \
         (your_choice == 2 and partner_choice == 3) or \
         (your_choice == 3 and partner_choice == 1):
        print("Вы победили!")
    else:
        print("Вы проиграли!")

play_game()