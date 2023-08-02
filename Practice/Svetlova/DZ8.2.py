def read_lines_from_file(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield line.rstrip('\n')

# Пример использования

filename = 'example.txt'

for line in read_lines_from_file(filename):
    print(line)