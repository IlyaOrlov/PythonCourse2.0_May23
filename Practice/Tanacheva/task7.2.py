class Duck:
    color = "Grey"

    def __init__(self, name=None, weight=0):
        self.name = name
        self.weight = weight

    def show_duck(self):
        print(f"Name: {self.name}.Weight: {self.weight}")

    def __repr__(self):
        return f" {self.color} duck with name {self.name}, with weight {self.weight}"

    def __lt__(self, other):
        return self.weight < other.weight

    def __gt__(self, other):
        return self.weight > other.weight

    def __eq__(self, other):
        return self.weight == other.weight

    def __ne__(self, other):
        return self.weight != other.weight

    def __add__(self, other):
        return Duck("Duck_Add", self.weight + other.weight)

    @staticmethod
    def print_crack():
        print('Crack')

    @classmethod
    def print_color(cls):
        print(f"Color of duck if {cls.color}")


d1 = Duck("Donald", 6)
print(d1)
d1.show_duck()
d2 = Duck("Dezzy", 4)
print(d1 < d2)
print(d1 > d2)
print(d1 == d2)
print(d1 != d2)
d3 = d1 + d2
print(d3)
d4 = Duck("SuperDuck", 6)
d5 = d1 + d2 + d4
print(d5)
