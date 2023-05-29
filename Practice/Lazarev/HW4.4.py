a1 = "Ты сам-то понял, что написал?"
a2 = "Аргументируй!"
a3 = "И?"
i = 0
while True:
    user_input = input("Напишите что-нибудь: ")
    i += 1
    if user_input == "хватит":
        break
    elif i % 3 == 1:
        print(a1)
    elif i % 3 == 0:
        print(a3)
    else:
        print(a2)