class Tank:
    def __init__(self, name, color, number):
        self._name = name
        self._color = color
        self._number = number

    def show(self):
        print(f"{self._name} {self._color} {self._number}")


class Army(Tank):
    def __init__(self, name, color, number, tanks):
        super().__init__(name, color, number)
        self._tanks = tanks


t1 = Tank("Tank1", "Green", 123)
a1 = Army("Tank2", "Grey", 777, (t1,))
lst = [t1, a1]
for i in lst:
    i.show()
