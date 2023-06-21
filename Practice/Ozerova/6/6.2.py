class Duck:
    color = "Yellow"
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    @staticmethod
    def sound():
        print("Crack")

    @classmethod
    def my_color(cls):
        print(f"My color {cls.color}.")

    def __repr__(self):
        return f"My name is {self.name}, my weight {self.weight} lb."

    def __lt__(self, other):
        return self.weight < other.weight

    def __gt__(self, other):
        return self.weight > other.weight

    def __eq__(self, other):
        return self.weight == other.weight

    def __ne__(self, other):
        return self.weight != other.weight

    def __add__(self, other):
        sum = self.weight + other.weight
        return Duck('Ponka', sum)


d1 = Duck("Ponka", 7850)
d2 = Duck("Lina", 3330)

print(d1 < d2)
print(d1 > d2)
print(d1 == d2)
print(d1 != d2)
dd = d1 + d2
print(dd)

