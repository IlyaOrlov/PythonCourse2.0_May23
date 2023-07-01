class Tank:
    def __init__(self, model, power, health):
        self.model = model  # модель
        self.power = power  # количество снарядов
        self.health = health  # количество жизней

    def show(self):
        print(f"Tank: model = {self.model}, power ={self.power}, health = {self.health}")

    def __ge__(self, other):
        return self.power >= other.power

    def __gt__(self, other):
        return self.power > other.power

    def __le__(self, other):
        return self.power <= other.power

    def __lt__(self, other):
        return self.power < other.power

    def __eq__(self, other):
        return self.power == other.power

    def kill_tank(self, blows):
        if self.health - blows == 0:
            print(f"Танк {self.model} был убит")
        else:
            print(f"Количество жизней у танка {self.model}: {self.health - blows}")


tank1 = Tank('T34', 56, 5)
tank2 = Tank('Tiger', 43, 3)
tank1.show()
tank2.show()
# сколько жизней осталось, после попаданий в танк
tank1.kill_tank(5)
tank2.kill_tank(2)

# сравнение танков по мощности
print(f"Танк {tank1.model} мощнее танка {tank2.model}: {tank1>tank2}")
