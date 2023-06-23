class CoordinatesError(Exception):
    pass


class Coordinates:
    def __init__(self, x, y):
        if isinstance(x, int) and isinstance(y, int):
            self._x = x
            self._y = y
        else:
            raise CoordinatesError(f"Bad attributes: {x=}, {y=}")

    def __repr__(self):
        return f"(x={self._x}, y={self._y})"

    def __add__(self, other):
        return Coordinates(self._x + other._x, self._y + other._y)


try:
    c1 = Coordinates(10, 20)
    c2 = Coordinates("30", "40")
    z = c1 + c2
    print(z)
finally:
    print("Happy end")
