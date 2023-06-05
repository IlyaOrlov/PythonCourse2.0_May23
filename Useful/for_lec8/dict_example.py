d = {}
while (i := input("Введите слово: ")) != "stop":
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

print(d)
