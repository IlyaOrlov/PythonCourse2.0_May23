# Игра "Камень, ножницы, бумага"
# наверное я пошел по самому сложному пути
# в дальнейшем подумаю, как можно оптимизировать этот код))
import random


def fun():
    ans_list = ["КАМЕНЬ", "НОЖНИЦЫ", "БУМАГА"]
    y = random.choice(ans_list)
    return y


print('Сыграем в "Камень, ножницы, бумага" ?\n'
      'Будем играть, пока тебе не надоест! Если ты устал, просто напиши "устал".')
while (x := input('Введи значение: ').upper()) != "УСТАЛ":
    if x == "КАМЕНЬ" or x == "НОЖНИЦЫ" or x == "БУМАГА":
        y = fun()
        if x == y:
            print(f"Машина: {y} = Ничья!")
        elif x == "КАМЕНЬ" and y == "БУМАГА":
            print(f"Машина: {y} = Победила машина!")
        elif x == "КАМЕНЬ" and y == "НОЖНИЦЫ":
            print(f"Машина: {y} = Победил человек!")
        elif x == "НОЖНИЦЫ" and y == "БУМАГА":
            print(f"Машина: {y} = Победил человек")
        elif x == "НОЖНИЦЫ" and y == "КАМЕНЬ":
            print(f"Машина: {y} = Победила машина!")
        elif x == "БУМАГА" and y == "КАМЕНЬ":
            print(f"Машина: {y} = Победил человек")
        elif x == "БУМАГА" and y == "НОЖНИЦЫ":
            print(f"Машина: {y} = Победила машина!")

    else:
        print('Неверное выражение!')
    continue
else:
    print('Ну, тогда отдохни! Игра закончена.')