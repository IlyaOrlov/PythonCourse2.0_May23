import random


def game():
    z = ["камень", "ножницы", "бумага"]
    v = random.choice(z)
    return v


print('Игра: "Камень, ножницы, бумага". Если устал, напиши стоп.')
while (x := input("Введи свой вариант: ").lower()) != "стоп":
    if x in ("камень", "ножницы", "бумага"):
        y = game()
        if x == y:
            print(f"Мой вариант: {y} - Ничья!")
        elif x == "камень":
            if y == 'ножницы':
                print(f"Мой вариант: {y} - Ты выиграл!")
            else:
                print(f"Мой вариант: {y} - Ты проиграл!")
        elif x == "ножницы":
            if y == "камень":
                print(f"Мой вариант: {y} - Ты проиграл!")
            else:
                print(f"Мой вариант: {y} - Ты выйграл!")
        elif x == "бумага":
            if y == "камень":
                print(f"Мой вариант: {y} - Ты выйграл!")
            else:
                print(f'Мой вариант: {y} - Ты проиграл!')
    else:
        print("Неверное выражение! Выбери: камень, ножницы или бумага!")
else:
    print('Игра окончена!')