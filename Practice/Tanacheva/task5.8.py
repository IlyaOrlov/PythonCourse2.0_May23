import random


def play():
    user_action = input("Выберите один предмет: камень, ножницы или бумага:")

    actions = ["камень", "ножницы", "бумага"]
    computer_action = random.choice(actions)
    print(f"Выбор компьютера: {computer_action}")

    if user_action == computer_action:
        print("Ничья!")
    elif user_action == "камень":
        if computer_action == "ножницы":
            print("Вы победили, камень тупит ножницы!")
        else:
            print("Вы проиграли, бумага оборачивает камень!")
    elif user_action == "ножницы":
        if computer_action == "камень":
            print("Вы проиграли, камень тупит ножницы!")
        else:
            print("Вы выиграли, ножницы режут бумагу!")
    elif user_action == "бумага":
        if computer_action == "камень":
            print("Вы выиграли, бумага оборачивает камень!")
        else:
            print("Вы проиграли, ножницы режут бумагу!")


while int(input("Хотите сыграть в игру, нажмите 1, если нет нажмите 2:")) == 1:
    play()
