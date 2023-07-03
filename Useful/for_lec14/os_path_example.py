import os.path


p = "2.txt"
if os.path.exists(p):
    f = open(p)
    print(f.read())
    f.close()
else:
    print("Файла не существует")


s = os.path.join("tmp", "1", "temp.file")
print(s)