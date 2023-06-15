import sys

def file_actions(file, choice, a, b):
    with open(file, 'r', encoding="utf8") as f:
        data = f.read()
        #print(data)
        if k == 1:
            if a in data:
                data = data.replace(a, b)
                print(f"В файле {file} присутствует символ(ы) табуляции и он(и) заменены на 4 пробела")
            else:
                print(f"В файле {file} отсутствует символ(ы) табуляции, закрываем файл")
                sys.exit(0)
        else:
            if b in data:
                data = data.replace(b, a)
                print(f"В файле {file} присутствуеn(-ют) 4 пробела и он(и) заменены на символ табуляции")
            else:
                print(f"В файле {file} отсутствует символы  - 4 пробела, закрываем файл")
                sys.exit(0)
    with open(file, 'w', encoding="utf8") as f:
        f.write(data)


FILE_NAME = 'primer.txt'
A = '\t'
B = '    '
t = (1, 2)
while (k := int(input(f"Выбери, действие с файлом {FILE_NAME}:\n1 - заменить все табуляции на 4 пробела\n2 - или заменить 4 пробела на табуляцию\n>>:"))) not in t:
    print("Повторите ввод!:")
file_actions(FILE_NAME, k, A, B)
