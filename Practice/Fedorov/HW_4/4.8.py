import random

tableWin = [["ножницы", "бумага", "Ты"],
            ["ножницы", "камень", "Я"],
            ["камень", "бумага", "Я"],
            ["камень", "ножницы", "Ты"],
            ["бумага", "камень", "Ты"],
            ["бумага", "ножницы", "Я"]]

print("Сыграем в камень ножницы бумага? Если устали напишите: хватит")
lst = ["камень", "ножницы", "бумага"]

while not (player1 := input("Введите камень ножнницы или бумага: ")).lower() == "хватит":
    if player1 not in lst:
        print("Ха-ха ты проиграл! Вводить можно только 3 возможных варианта")
        continue
    player2 = random.choice(lst)
    if player2 == player1.lower().replace(" ", ""):
        print(f"Ничья! У обоих игроков {player2}")
        continue
    for i in range(len(tableWin)):
        if player1 == tableWin[i][0] and player2 == tableWin[i][1]:
            print(f"Ура! {tableWin[i][2]} победил!")
            break
