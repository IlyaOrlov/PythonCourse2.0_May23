def myfilereader(filepath):
    with open(filepath, "r") as f:
        for i in f:
            yield i


for i in myfilereader("1.txt"):
    print(i)
