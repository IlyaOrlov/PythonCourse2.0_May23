def read_file_lines(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield line.rstrip()


# Пример использования генератора
file_path = 'example.txt'  # Путь к файлу

for line in read_file_lines(file_path):
    print(line)
    