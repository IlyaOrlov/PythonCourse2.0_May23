class Tank:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def shoot(self, target):
        print(f"{self.name} наносит {self.damage} урона {target.name}")
        target.health -= self.damage


class BattleField:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tanks = []

    def add_tank(self, tank):
        self.tanks.append(tank)
        print(f"{tank.name} добавлен на поле боя")

    def start_battle(self):
        print("Битва началась!")
        while len(self.tanks) > 1:
            attacker = self.tanks[0]
            defender = self.tanks[1]

            attacker.shoot(defender)

            if defender.health <= 0:
                print(f"{defender.name} уничтожен!")
                self.tanks.remove(defender)

            self.tanks.reverse()

        print(f"{self.tanks[0].name} победил в битве!")


# Создание экземпляров классов
tank1 = Tank("Тiger", 100, 20)
tank2 = Tank("Leopard", 150, 15)
tank3 = Tank("Т-34", 120, 25)

battlefield = BattleField(10, 10)

battlefield.add_tank(tank1)
battlefield.add_tank(tank2)
battlefield.add_tank(tank3)

battlefield.start_battle()
