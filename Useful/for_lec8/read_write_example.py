with open("композиция_vs_наследование.txt", "w") as f1:
    f1.write('abc')

with open("композиция_vs_наследование.txt", "r") as f2:
    res = f2.read()
    print(res)
