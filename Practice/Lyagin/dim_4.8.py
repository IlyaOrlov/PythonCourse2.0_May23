import random

m = 0
n = 0

def win(chel, comp):
    if chel == comp:
        return "Ничья"
    elif chel == 1 and comp == 2 or chel == 2 and comp == 3 or chel == 3 and comp == 1:
        return "Победил человек!"
    else:
        return "Победил компьютер!"


while True:
    chel = int(input("1 - камень, 2 - ножницы, 3 - бумага, 4 - конeц игры "))
    if chel == 4:
        print(f"Стоп игра\nОбщий счёт: Человек {m} Компьютер {n} ")
        break
    elif chel == 1:
        print("Человек выбрал камень")
    elif chel == 2:
        print("Человек выбрал ножницы")
    elif chel == 3:
        print("Человек выбрал бумагу")
    else:
        print("Ввели что то не то. Введите цифру от 1 до 4")
        continue    # наконец то нашёл , чего мне так не хватало)


    comp = random.randint(1, 3)
    if comp == 1:
        print("Компьютер выбрал камень")
    elif comp == 2:
        print("Компьютер выбрал ножницы")
    else:
        print("Компьютер выбрал бумагу")

    winner = win(chel,comp)
    if winner == "Победил человек!":
        m += 1
    elif winner == "Победил компьютер!":
        n += 1
    print(winner)
