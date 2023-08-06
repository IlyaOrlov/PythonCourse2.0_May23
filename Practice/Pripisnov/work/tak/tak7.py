import os


lst = []
for fname in os.listdir('.'):
    if fname.startswith("file"):
        with open(fname) as f:
            s = f.read().strip()
            if (i := int(s)) % 10 == 0:
                lst.append(i)

print(lst)
