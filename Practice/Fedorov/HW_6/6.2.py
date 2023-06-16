class Duck:
    color = "White"

    def __init__(self, name=None, weight=0):
        self._name = name
        self._weight = weight

    def __repr__(self):
        return f"{self._name} {self.color}"

    def __ge__(self, other):
        return self._weight >= other._weight

    def __gt__(self, other):
        return self._weight > other._weight

    def __eq__(self, other):
        return self._weight == other._weight

    def __ne__(self, other):
        return self._weight != other._weight

    def __add__(self, other):
        return self._weight + other._weight

    @staticmethod
    def hello():
        print("Сrack")

    @classmethod
    def which_color(cls):
        print(cls.color)

    def say_hello(self):
        print(f"{self._name} {self._weight}")


x = Duck("Беляш", 10)
x1 = Duck("Марта", 10)
print(x < x1)
print(x + x1)
x.say_hello()
