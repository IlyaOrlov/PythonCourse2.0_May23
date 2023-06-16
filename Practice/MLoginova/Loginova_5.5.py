def file_actions(file, choice, tab, spase):
    with open(file, 'r', encoding="utf8") as f:
        data = f.read()
        #print(data)
        if k == 1:
            if tab in data:
                data = data.replace(tab, spase)
                print(f"В файле {file} присутствует символ(ы) табуляции и он(и) заменены на 4 пробела")
            else:
                print(f"В файле {file} отсутствует символ(ы) табуляции, закрываем файл")
                return
        else:
            if spase in data:
                data = data.replace(spase, tab)
                print(f"В файле {file} присутствуеn(-ют) 4 пробела и он(и) заменены на символ табуляции")
            else:
                print(f"В файле {file} отсутствует символы  - 4 пробела, закрываем файл")
                return
    with open(file, 'w', encoding="utf8") as f:
        f.write(data)


FILE_NAME = 'primer.txt'
TAB_SYM = '\t'
SPACE_SYM = '    '
t = (1, 2)
while (k := int(input(f"Выбери, действие с файлом {FILE_NAME}:\n1 - заменить все табуляции на 4 пробела\n2 - или заменить 4 пробела на табуляцию\n>>:"))) not in t:
    print("Повторите ввод!:")
file_actions(FILE_NAME, k, TAB_SYM, SPACE_SYM)
