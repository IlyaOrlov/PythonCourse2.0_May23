# Написать приложение – игру "камень, ножницы, бумага".

import random

print("Вы попали в игру 'Камень, ножницы, бумага', Если надоест играть, напишите: хватит")
comp = random.choice(["камень", "ножницы", "бумага"])

while (answer := input("Выберете камень, ножницы или бумага: ").lower()) != "хватит":
    print(f"Выбор компьютера: {comp}")
    if answer == comp:
        print("Ничья")
    elif answer == "камень" and comp == "ножницы":
        print("Вы выйграли")
    elif answer == "камень" and comp == "бумага":
        print("Вы проиграли")
    elif answer == "ножницы" and comp == "камень":
        print("Вы проиграли")
    elif answer == "ножницы" and comp == "бумага":
        print("Вы выйграли")
    elif answer == "бумага" and comp == "ножницы":
        print("Вы проиграли")
    elif answer == "бумага" and comp == "камень":
        print("Вы выйграли")
