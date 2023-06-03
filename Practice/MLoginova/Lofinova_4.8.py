#Написать приложение – игру "камень, ножницы, бумага".
import random

lst = [0, 1, 2]
print("Привет! Давай сыграем в игру - 'камень, ножницы, бумага'\nЧтобы закончить игру напиши - СТОП или стоп.")
while not (player1 := input("\nВведите цифру соответствующую выбору:\n0 - камень, 1 - ножницы, 2 - бумага: ").lower()) =="стоп":
    player1 = int(player1)
    if player1 not in lst:
        print(f"Вы ввели число  - {player1} НЕ удовлетворяющее возможным вариантам. Повторите попытку ввода: ")
        continue
    player2 = random.choice(lst)
    if player1 == player2:
        print(f"Победила дружба! У нас с тобой - {player2}")
        continue
#Если камень тупит ножницы или ножницы режут бумагу или бумага оборачивает камень
    elif (player1 == 0 and player2 == 1) or (player1 == 1 and player2 == 2) or (player1 == 2 and player2 == 0):
        print(f"Позравляем!Ты - победил!Ты ввёл {player1}, а у меня {player2}")
    else:
        print(f"Увы. Ты проиграл. Ты ввёл {player1}, а у меня {player2}")
