answers = ["Ты сам‐то понял, что написал?","Аргументируй","И?"]
request = ""
i = 0
while request.lower() != "хватит":
    request = input("Введите Ваш запрос: ")
    print(answers[i])
    if i <= len(answers)-2:
        i += 1
    else:
        i = 0
print(f"Ввод запросов завершён, так как Вы ввели слово - {request}")
