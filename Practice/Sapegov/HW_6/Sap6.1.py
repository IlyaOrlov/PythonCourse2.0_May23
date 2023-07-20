class HeavyTank:
    strength = 100

    def __init__(self, model, weight, power):
        self.model = model
        self.weight = weight
        self.power = power

    def description(self):
        print(f'Танк: {self.model}, {self.weight} т., {self.power} л.с.')

    def damage_taken(self, damage):
        self.strength -= damage


class LegendaryTank:
    strength = 100

    def __init__(self, model, weight, power, creation):
        self.model = model
        self.weight = weight
        self.power = power
        self.creation = creation

    def description(self):
        print(f'Танк: {self.model}, {self.weight} т., {self.power} л.с., {self.creation} г.')

    def damage_taken(self, damage):
        self.strength -= damage


tank1 = HeavyTank('Т-72Б', 30, 1300)
tank1.damage_taken(15)
tank2 = HeavyTank('Leopard', 25, 1200)
tank2.damage_taken(57)
tank3 = LegendaryTank('Т-34', 10, 1000000, 1943)
tank3.damage_taken(0)

tank1.description()
print(f'Оставшаяся прочность: {tank1.strength}%')
print('_________________________________')
tank2.description()
print(f'Оставшаяся прочность: {tank2.strength}%')
print('_________________________________')
tank3.description()
print(f'Оставшаяся прочность: {tank3.strength}%')
