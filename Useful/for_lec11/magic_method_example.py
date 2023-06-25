class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"{self.x=}, {self.y=}")

    def __add__(self, other):
        x1 = self.x + other.x
        y1 = self.y + other.y
        return Coordinates(x1, y1)

    def __sub__(self, other):
        x1 = self.x + other.x
        y1 = self.y + other.y
        return Coordinates(x1, y1)


c1 = Coordinates(10, 20)
c2 = Coordinates(100, 200)
z = c1 - c2
print(z)
z.show()

