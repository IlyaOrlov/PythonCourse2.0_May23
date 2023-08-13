def file_reader(path):
    with open(path) as file:
        for i in file:
            yield i


for i in file_reader("D:/123.txt"):
    print(i)