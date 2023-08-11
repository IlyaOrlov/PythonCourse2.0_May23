# Написать генератор для построчного чтения файла.

def read_line(name_file):
    with open(name_file, 'r') as file:
        for line in file:
            yield line

name_file = "test.txt"
for line in read_line(name_file):
    print(line)
