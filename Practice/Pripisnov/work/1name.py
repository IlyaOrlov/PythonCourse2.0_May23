import random


s = "бвгдж"
g = "аеёюи"
x1 = random.choice(s)
y1 = random.choice(g)
x2 = random.choice(s)
y2 = random.choice(g)
print(x1 + y1 + x2 + y2)