answer1 = "Ты сам‐то понял, что написал?"
answer2 = "Аргументируй"
answer3 = "И?"
i = 2
while (q := input('Введите вопрос:')).lower() != "хватит":
    i += 1
    if i % 3 == 0:
        print(answer1)
    if i % 3 == 1:
        print(answer2)
    if i % 3 == 2:
        print(answer3)

print("")
print("Игра окончена!")
