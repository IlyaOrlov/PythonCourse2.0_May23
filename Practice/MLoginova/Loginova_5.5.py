def file_actions(f_name, k):
    with open(f_name, 'r', encoding="utf8") as f:
        data = f.read()
        #print(data)
        if k == 1:
            if a in data:
                data = data.replace(a, b)
                print(f"В файле {f_name} присутствует символ(ы) табуляции и он(и) заменены на 4 пробела")
            else:
                print(f"В файле {f_name} отсутствует символ(ы) табуляции, закрываем файл")
                f.close()
        else:
            if b in data:
                data = data.replace(b, a)
                print(f"В файле {f_name} присутствуеn(-ют) 4 пробела и он(и) заменены на символ табуляции")
            else:
                print(f"В файле {f_name} отсутствует символы  - 4 пробела, закрываем файл")
                f.close()
    with open(f_name, 'w', encoding="utf8") as f:
        f.write(data)


f_name = 'primer.txt'
a = '\t'
b = '    '
t = (1, 2)
while (k := int(input(f"Выбери, действие с файлом {f_name}:\n1 - заменить все табуляции на 4 пробела\n2 - или заменить 4 пробела на табуляцию\n>>:"))) not in t:
    print("Повторите ввод!:")
file_actions(f_name, k)
