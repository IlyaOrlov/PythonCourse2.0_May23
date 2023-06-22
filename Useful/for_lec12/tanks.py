class Tank:
    _x = 0
    _speed = 0
    _power = 0

    def shoot(self):
        pass

    def show(self):
        print(f'Tank {type(self)} at {self._x}')

    def move(self):
        self._x += self._speed

    def __lt__(self, other):
        return self._power < other._power


class T34(Tank):
    _speed = 30
    _power = 30

    def shoot(self):
        print("Ba-bah")


class Tiger(Tank):
    _speed = 20
    _power = 40

    def shoot(self):
        print("Ba-ba-bah")


class T90(Tank):
    _speed = 40
    _power = 40

    def shoot(self):
        print("Ba-buh")


if __name__ == "__main__":
    tanks = [T34(), Tiger(), T90()]
    while True:
        for x, y in enumerate(tanks):
            print(f"{x} - {type(y)}")
        i = int(input('Input tank index:'))
        tanks[i].show()
        tanks[i].move()
        tanks[i].shoot()
        tanks[i].show()
