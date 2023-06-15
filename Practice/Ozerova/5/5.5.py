str1 = input("Укажите где находится документ?")
str2 = input("Введите для четырех пробелов - 1, а для табуляции - 2")


with open(str1) as document:
    x = document.read()
    if str2 == "1":
        x = x.replace("\t", "    ")
    else:
        x = x.replace("    ", "\t")
with open(str1, "w") as new_document:
    new_document.write(x)
