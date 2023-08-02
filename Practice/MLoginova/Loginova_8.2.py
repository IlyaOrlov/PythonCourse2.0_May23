#  Написать генератор для построчного чтения файла.
def read_file(file):
    with open(file, 'r', encoding="utf8") as f:
        for res in f:
            yield res


MY_FILE = '8_2.txt'
for i in read_file(MY_FILE):
    print(i)
