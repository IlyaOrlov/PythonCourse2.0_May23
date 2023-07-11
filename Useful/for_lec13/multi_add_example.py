class Coordinates:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __repr__(self):
        return f"(x={self._x}, y={self._y})"

    def __add__(self, other):
        return Coordinates(self._x + other._x, self._y + other._y)


c1 = Coordinates(10, 20)
c2 = Coordinates(30, 40)
c3 = Coordinates(50, 60)
z = c1 + c2 + c3
print(z)
