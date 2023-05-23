while (i := input("Введите слово: ")) != "stop":
    if i == "привет":
        print("привет")
    elif i == "пока":
        print("пока")
        break
    elif i == "как дела?":
        print("хорошо")
        continue
    print("Очередная итерация цикла")
else:
    print("Конец цикла!")
