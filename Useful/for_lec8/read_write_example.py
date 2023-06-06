with open("1.txt", "w") as f1:
    f1.write('abc')

with open("1.txt", "r") as f2:
    res = f2.read()
    print(res)
