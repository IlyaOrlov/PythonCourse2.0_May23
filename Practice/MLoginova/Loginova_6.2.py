class Duck:
    color = "white"

    def __init__(self, name,  weight):
        self.name = name if name else self.generate_name()
        self.weight = weight

    @staticmethod
    def say_crack():
        print("Сrack")

    @classmethod
    def crack_colors(cls):
        print(cls.color)

    #метод, выводящий имя и вес утки
    def __repr__(self):
        return f"Name duck  - {self.name}, weight - {self.weight}"

    def __lt__(self, other):
        return self.weight < other.weight

    def __ne__(self, other):
        return self.weight != other.weight

    def __add__(self, other):
        return Duck("Total weight", self.weight + other.weight)

class RiverDucks(Duck):
    color = "black"


d1 = Duck("Stepa", 3500)
d1.say_crack()
d1.crack_colors()
print(d1)
print("###################")
d2 = Duck("Gora", 1500)
d2.say_crack()
d2.crack_colors()
print(d2)
print("###################")
d3 = RiverDucks("Cherry", 2500)
d3.say_crack()
d3.crack_colors()
print(d3)
print("###################")
print(f"d1 < d2 - {d1 < d2}")
print(f"d2 < d3 - {d2 < d3}")
print(f"d1 != d2 - {d1 != d2}")
print(f"d1 + d2 - {d1 + d2}")
