lst = [1, 6, 8, 4, 5]
lst.sort()
print(lst)

class Tank:
    def __init__(self, power, speed):
        self.power = power
        self.speed = speed

    def __lt__(self, other):
        if self.power == other.power:
            return self.speed < other.speed
        else:
            return self.power < other.power

    def __repr__(self):
        return f"Tank: p:{self.power}, s:{self.speed}"


lst = [Tank(10, 20), Tank(40, 30), Tank(50, 60)]
lst1 = [[1, 2], [3, 4], [1, 3]]
lst1.sort()
print(lst1)


def fun(x):
    return x.speed

lst.sort(key=lambda x: x.speed)
print(lst)
