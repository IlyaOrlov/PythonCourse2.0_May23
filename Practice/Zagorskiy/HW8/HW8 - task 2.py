# Написать генератор для построчного чтения файла.
def read_str(file):
    with open(file, 'r', encoding='utf-8') as f:
        for j in f:
            yield j


file = read_str('reader_file.txt')
for i in file:
    print(i)

