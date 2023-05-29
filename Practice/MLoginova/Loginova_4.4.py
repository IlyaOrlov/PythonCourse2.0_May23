answers = ["Ты сам‐то понял, что написал?","Аргументируй","И?"]
request = ""
i = 0
while (request :=input("Введите Ваш запрос: ")).lower() != "хватит":
    print(answers[i])
    if i < len(answers)-1:
        i += 1
    else:
        i = 0
print(f"Ввод запросов завершён, так как Вы ввели слово - {request}")
