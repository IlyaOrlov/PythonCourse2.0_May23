def gen_filereader(x):
    with open(x) as f:
        for y in f:
            yield y


name = 'for8.2.txt'
for i in gen_filereader(name):
    print(i)
