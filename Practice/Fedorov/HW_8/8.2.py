def read_file(path):
    with open(path, 'r', encoding="utf-8") as my_file:
        for line in my_file:
            yield line


f = read_file("file.txt")
next(f)
next(f)
for i in f:
    print(i)
# Пока мне не понятно где я бы мог их использовать
