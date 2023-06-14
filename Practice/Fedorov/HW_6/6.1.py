
class Tanks:

    def __init__(self, name, model):
        self.name = name
        self.model = model
        self.hp = 100
        self.dmg = 10

    def __sub__(self, other):
        if isinstance(other, Tanks):
            print(f"{self.name} атакует {other.name}")
            other.hp = other.hp - self.dmg

    def say_about_me(self):
        print(f"Имя: {self.name} {self.model}")
        print(f"HP: {self.hp}")
        print(f"dmg: {self.dmg}")


t1 = Tanks("Tank1", "T-34")
t1.say_about_me()

t2 = Tanks("Tank2", "KF-51")
t2.say_about_me()
t1 - t2
t1.say_about_me()
t2.say_about_me()

