class Tank:
    state = 100

    def __init__(self, model, power_attack, dis_attack):
        self.model = model
        self.power_attack = power_attack
        self.dis_attack = dis_attack

    def review(self):
        print(f'танк {self.model} '
              f'\n   мощность удара: {self.power_attack}  дальность удара: {self.dis_attack}  состояние: {self.state}')


ob_1 = Tank('Т-34', 10, 1000)
ob_1.review()
ob_2 = Tank('Т-90', 40, 4000)
ob_2.review()
