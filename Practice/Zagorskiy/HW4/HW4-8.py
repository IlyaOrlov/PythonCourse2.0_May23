# Игра "Камень, ножницы, бумага"
# наверное я пошел по самому сложному пути
# в дальнейшем подумаю, как можно оптимизировать этот код))
import random


print('Сыграем в "Камень, ножницы, бумага" ?\n'
      'Будем играть, пока тебе не надоест! Если ты устал, просто напиши "устал".')

ans_list = ["КАМЕНЬ", "НОЖНИЦЫ", "БУМАГА"]

while (x := input('Введи значение: ').upper()) != "УСТАЛ":
    if x in ans_list:
        y = random.choice(ans_list)
        if x == y:
            print(f"Машина: {y} = Ничья!")
        elif x == "КАМЕНЬ":
            if y == "БУМАГА":
                print(f"Машина: {y} = Победила машина!")
            else:
                print(f"Машина: {y} = Победил человек!")
        elif x == "НОЖНИЦЫ":
            if y == "КАМЕНЬ":
                print(f"Машина: {y} = Победила машина!")
            else:
                print(f"Машина: {y} = Победил человек!")
        elif x == "БУМАГА":
            if y == "НОЖНИЦЫ":
                print(f"Машина: {y} = Победила машина!")
            else:
                print(f"Машина: {y} = Победил человек!")
    else:
        print('Неверное выражение!')
else:
    print('Ну, тогда отдохни! Игра закончена.')
