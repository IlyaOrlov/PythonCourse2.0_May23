import random


def play_game():
    x =  ('камень', 'ножницы', 'бумага')

    while True:
        igrok_y = input(f"Выберите: {x} (или 'выход' для завершения):").lower()

        if igrok_y == 'выход':
            break

        if igrok_y not in x:
            print("Некорректный выбор. Попробуйте еще раз.")
            continue

        computer_z = random.choice(x)

        print("Вы выбрали:", igrok_y)
        print("Компьютер выбрал:", computer_z)

        if igrok_y == computer_z:
            print("Ничья!")
        elif (igrok_y == 'камень') and (computer_z == 'ножницы'):
            print("Вы победили!")
        elif (igrok_y == 'ножницы') and (computer_z == 'бумага'):
            print("Вы победили!")
        elif (igrok_y == 'бумага') and (computer_z == 'камень'):
            print("Вы победили!")
        else:
            print("Компьютер победил!")

        print()

play_game()

