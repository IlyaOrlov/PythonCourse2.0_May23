import random
class Tanks:

    def __init__(self, name=None):
        self.name = name if name else self.generate()
        self.hp, self.dmg = self.generate_hp_dmg()

    def __ge__(self, other):
        return self.hp >= other.hp

    def __gt__(self, other):
        return self.hp > other.hp

    def __eq__(self, other):
        return self.hp == other.hp

    def __ne__(self, other):
        return self.hp != other.hp

    def say_charactiristic(self):
        print(f"Имя: {self.name}")
        print(f"HP: {self.hp}")
        print(f"dmg: {self.dmg}")

    def attack(self, other):
        other.hp -= self.dmg

    def heal(self):
        self.hp += self.random_heal()

    @staticmethod
    def generate():
        return f"Tank-{random.randint(1, 10)}"

    @staticmethod
    def generate_hp_dmg():
        hp = int(random.randint(5, 10) * 10)
        return hp, 100 // (hp / 10)
    @staticmethod
    def random_heal():
        hp = random.choice([True, False])
        if hp:
            heal = 10
        else:
            heal = 0
        return heal


t1 = Tanks()
t2 = Tanks()
t1.attack(t2)
t2.attack(t1)
t1.heal()
t2.heal()
t1.say_charactiristic()
t2.say_charactiristic()
print(t1 > t2)




