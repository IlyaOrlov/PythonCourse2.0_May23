answers = ["Ты сам‐то понял, что написал?","Аргументируй","И?"]
request = ""
i = 0
#print(len(answers))
while request.lower() != "хватит" and i <= len(answers)-1:
    request = input("Введите Ваш запрос: ")
    if request.lower() != "хватит":
        print(answers[i])
        i += 1
print(f"Вы остановили ввод символов, введя {request} или ответы из списка закончились!=)")
