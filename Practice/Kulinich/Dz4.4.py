y = "Ты сам‐то понял, что написал?"
d = "Аргументируй"
s = "И?"
x=1
while (input("Ведите ваш вопрос  ")) != "хватит":
    if x == 1:
        print(y)
    elif x == 2:
        print(d)
    elif x == 3:
        print(s)
    x += 1
    if x >3:
        x=1