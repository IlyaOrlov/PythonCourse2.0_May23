# Спроектировать классы (один или несколько) для игры в танки и создать экземпляры этих классов.
class Tanks:
    def __init__(self, name="", health=0, damage=0, armor=0):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor

    def show(self):
        if self.bonus:
            print(f"|{self.name} {self.health} {self.damage} {self.armor} |{self.bonus}|")
        else:
            print(f"|{self.name} {self.health} {self.damage} {self.armor}|")


class HeavyTank(Tanks):
    def __init__(self, name, health, damage, armor, bonus):
        super().__init__(self, name, health, damage)
        self.bonus = bonus


class MiddleTank(Tanks):
    def __init__(self, name, health, damage, armor, bonus=""):
        super().__init__(self, name, health, damage)
        self.bonus = ""


class LightTank(Tanks):
    def __init__(self, name, health, damage, armor, bonus):
        super().__init__(self, name, health, damage,)
        self.bonus = bonus


t1 = HeavyTank("A1 AAbrams", 500, 150, 90, "armor_bonus = 15")
t2 = MiddleTank("Panther", 350, 100, 65)
t3 = MiddleTank("M48 Patton", 400, 110, 70)
t4 = LightTank("LTTB", 200, 70, 40, "recon_bonus = 30")

lst = [t1, t2, t3, t4]
for i in lst:
    i.show()

