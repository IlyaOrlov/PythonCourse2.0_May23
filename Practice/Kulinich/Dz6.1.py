class Tank:
    color = "khaki"

    def __init__(self, model, caliber, weight, price):
        self.model = model
        self.caliber = caliber
        self.weight = weight
        self.price = price

    def show(self):
        print(f'Танк {self.model} :  Калибр: {self.caliber} мм., Вес: {self.weight} т., Цена: {self.price} млн.$. ')


tank1 = Tank('Т-72', 125, 46, 3)
tank1.show()
tank2 = Tank('Т-80', 125, 42.5, 6)
tank2.show()
tank2 = Tank('Т-90', 125, 46,2.5)
tank2.show()