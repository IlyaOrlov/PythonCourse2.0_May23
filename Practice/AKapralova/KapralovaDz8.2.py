# Написать генератор для построчного чтения файла.
def read_by_line(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line


for line in read_by_line('2txt'):
    print(line)
