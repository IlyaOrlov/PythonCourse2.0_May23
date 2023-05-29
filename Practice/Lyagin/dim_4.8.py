import random


m = 0
n = 0
while True:
        chel = int(input("1 - камень, 2 - ножницы, 3 - бумага, 4 - конeц игры "))
        if chel == 4:
                print(f"Стоп игра\nОбщий счёт: Человек {m} Компьютер {n} ")
                break
        if chel == 1:
                print("Вы выбрали камень")
        if chel == 2:
                print("Вы выбрали ножницы")
        if chel == 3:
                print("Вы выбрали бумагу")


        comp = random.randint(1, 3)
        if comp == 1:
                print("Компьютер выбрал камень")
        if comp == 2:
                print("Компьютер выбрал ножницы")
        if comp == 3:
                print("Компьютер выбрал бумагу")

        if chel == comp:
                s = 0
        if chel == 1 and comp == 2:
                s = 1
        if chel == 1 and comp == 3:
                s = 2
        if chel == 2 and comp == 1:
                s = 2
        if chel == 2 and comp == 3:
                s = 1
        if chel == 3 and comp == 1:
                s = 1
        if chel == 3 and comp == 2:
                s = 2
        if s == 0:
                print("Ничья!)")
        if s == 1:
                print("Победил человек!")
                m += 1
        if s == 2:
                print("Победил компьютер!")
                n += 1
