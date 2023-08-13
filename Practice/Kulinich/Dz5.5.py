str1 = input("Введите путь к файлу ")
str2 = input("Для замены четырех пробелов табуляцией введите 0, для замены табулиции введите любой символ ")


with open(str1) as dok:
    repldok = dok.read()
    if str2 == "0":
        repldok = repldok.replace("    ", "\t")
    else:
        repldok = repldok.replace("\t", "    ")
with open(str1, "w") as dok2:
     dok2.write(repldok)



