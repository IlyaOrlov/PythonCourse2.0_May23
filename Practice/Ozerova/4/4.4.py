x = 1
while (y := input("Привет: ")) != "хватит":
    if x == 1:
        print("Ты сам-то понял, что написал?")
        x += 1
    elif x == 2:
        print("Аргументируй")
        x += 1
    else:
        print("И?")
        x = 1
else:
    print("Пока!")
