#Реализовать цикл, формирующий число из вводимых пользователем символов, пока не
#будет введено слово “stop” (или “Stop”, или “STOP”). Если пользователь ввел не числовой
#символ, вывести предупреждение и запросить новый символ.
a = ""
x = ""
while x.lower() != "stop":
    x = input("Введите числовой символ: ")
    if x.isdecimal() and len(x) == 1:
        a = a + x
        print(f"Сформированное число: {a}")
    elif x.lower() == "stop":
        break
    else:
        print(f"Предупреждение!\nВы ввели НЕ число или НЕ 1 символ. Вы ввели: {x}\n")
print(f"Вы остановили ввод символов, введя {x}")
