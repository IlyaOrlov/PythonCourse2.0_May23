a1 = "Ты сам-то понял, что написал."
a2 = "Аргументируй."
a3 = "И?"
print("Отгадай загадку. Зимой и летом, одним цветом? Если сдаешся, напиши хватит.")
x = input("Твой вариант: ")
y = 0
while x.lower() != "хватит":
    if y == 0:
        print(a1)
        y += 1
    elif y == 1:
        print(a2)
        y += 1
    else:
        print(a3)
        y = 0

    x = input("Введите утверждение: ")
else:
    print("Не расстраивайся! Может в другой раз получится!")
