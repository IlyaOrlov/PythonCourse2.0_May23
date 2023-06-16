class Worker:
    def __init__(self, base):
        self.base = base


class Multiplier(Worker):
    def __call__(self, num):
        return self.base * num


class Deleter(Worker):
    def __call__(self, num, option="*"):
        return num / self.base


m = Multiplier(10)
print(m(50))
print(m(20))
m = Deleter(10)
print(m(50))
print(m(20))