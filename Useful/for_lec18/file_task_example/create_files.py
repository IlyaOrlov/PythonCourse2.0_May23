import random



for i in range(50):
    name = f"file_{i}"
    with open(name, "w") as f:
        f.write(str(random.randint(1, 1000)))

