class FileLineReader:
    def __init__(self, filename):
        self.filename = filename

    def read_lines(self):
        with open(self.filename, 'r') as file:
            for line in file:
                yield line.rstrip('\n')

# Пример использования

filename = 'example.txt'
line_reader = FileLineReader(filename)

for line in line_reader.read_lines():
    print(line)
