# Реализовать функциональность, которая бы “сворачивала” и “разворачивала” символы табуляции
# в файле. То есть, на вход передается файл, необходимо заменить все символы табуляции на
# четыре пробела, либо же заменить все комбинации из четырех символов пробела на символ
# табуляции (в зависимости от опции, указанной пользователем).

def file_change (name, x):
    with open(name, "r") as filename:
        fileread = filename.read()
        if action == "1":
            fileread = fileread.replace('\t', '    ')
        else:
            fileread = fileread.replace('    ', '\t')
    with open(name, "w") as new_filename:
        new_filename.write(fileread)


action = int(input("Для замены табуляции на четыре символа пробела в файле нажмите 1, "
                   "для замены символов пробела на табуляцию нажмите 2: "))
file = "test.txt"
file_change(file, action)