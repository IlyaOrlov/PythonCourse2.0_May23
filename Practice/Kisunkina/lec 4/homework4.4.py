lst = ["Ты сам - то понял, что написал?", "Аргументируй", "И?"]
i = 0

while (answer := input("Напиши мне что-нибудь: ").lower()) != "хватит":
    print(f"{lst[i]}")
    i += 1
    if i == 3:
        i = 0
