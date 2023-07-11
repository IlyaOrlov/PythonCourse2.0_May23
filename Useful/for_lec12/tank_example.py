class Tank:
    model = None

    def __init__(self, number, speed, health):
        self._number = number
        self._speed = speed
        self._health = health
        self._x = 0

    def show(self):
        print(f"I'm {type(self).model} at {self._x}")

    def move(self, value):
        self._x = value * self._speed

    def shoot(self):
        raise NotImplementedError


class T34(Tank):
    model = "T34"

    def shoot(self):
        print("Ba-bah")


class Tiger(Tank):
    model = "Tiger"

    def shoot(self):
        print("BA_BAH")


class TankNew(Tank):
    def shoot(self):
        print("my shoot")


t = TankNew(1, 3, 4)
t.shoot()


t1 = T34(123, 30, 10)
t2 = Tiger(321, 20, 20)
tank_list = [t1, t2]

while True:
    res = input(f"Выберите танк: {list(range(len(tank_list)))} или stop")
    if res.isdecimal():
        res = int(res)
        tank_list[res].show()
        tank_list[res].move(int(input("На сколько подвинуть: ")))
        tank_list[res].shoot()
        tank_list[res].show()
    else:
        break

