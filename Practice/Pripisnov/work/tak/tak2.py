class Multiplier:
    def __init__(self, base):
        self.base = base

    def __call__(self, num, option="*"):
        if option == "*":
            return self.base * num
        else:
            return num / self.base


m = Multiplier(10)
print(m(50))
print(m(20))
