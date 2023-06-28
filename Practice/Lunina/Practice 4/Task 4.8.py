import random


print("Привет! Давай сыграем в игру:'Камень, ножницы, бумага'")
game_list = ["камень", "ножницы", "бумага"]
pk_choice = random.choice(game_list)

while not (v1 := input("Сделайте выбор: ")).lower() in game_list:
    print("Вы ввели не то")

print(f"\nВы выбрали {v1}, компьютер выбрал {pk_choice}.\n")
if v1 == pk_choice:
    print("ничья")
elif v1 == "камень":
    if pk_choice == "ножницы":
        print("Вы выиграли: камень тупит ножницы")
    else:
        print("Вы проиграли: бумага накрывает камень")
elif v1 == "бумага":
    if pk_choice == "камень":
        print("Вы выиграли: бумага накрывает камень")
    else:
        print("Вы проиграли: ножницы разрезают бумагу")
elif v1 == "ножницы":
    if pk_choice == "камень":
        print("Вы проиграли: камень тупит ножницы")
    else:
        print("Вы выиграли: ножницы разрезают бумагу")
