class Tanks:
    name = "_"
    classification = "_"
    weight = "_"
    crew = 0
    speed = 0
    firing_range = 0

    def __init__(self, name1, classification1, weight1, crew1):
        self.name = name1
        self.classification = classification1
        self.weight = weight1
        self.crew = crew1
        self.speed = 50
        self.firing_range = 3

    def say_my_name(self):
        print(f"Перед вами танк: {self.name}, {self.classification}, {self.weight}, {self.crew}.")

    def add_speed(self, bonus):
        self.speed += bonus

    def add_firing_range(self, bonus):
        self.firing_range += bonus


t1 = Tanks("T-90ам", "Средний и основной танк", "48 т.", "3 чел")
t1.say_my_name()
t1.add_firing_range(1)
print(f"{t1.firing_range=}")
t2 = Tanks("T-72Б3", "Основной танк", "46,5 т.", "3 чел")
t2.say_my_name()
t2.add_speed(10)
print(f"{t2.speed=}")
t3 = Tanks("Т-62", "Средний и основной танк", "37 т.", "4 чел")
t3.say_my_name()
t3.add_speed(20)
t3.add_firing_range(2)
print(f"{t3.firing_range=}")
print(f"{t3.speed=}")
