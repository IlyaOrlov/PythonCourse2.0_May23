class Bankomate:
    def __init__(self, name, balance=0):
        self._name = name
        self._balance = float(balance)

    def AboutBankomate(self):
        print(f'Банкомат: {self._name}')

    def process(self):
        print('Банкомат осуществляет выдачу и получение наличных')

    def get_money(self, money):
        self._balance += money

    def give_money(self, money):
        if self._balance - money < 0:
            print(f'На текущий момент в банкомате {self._name} недостаточно денежных средств')
        else:
            self._balance -= money


class FirstBankomate(Bankomate):
    pass


class SecondBankomate(Bankomate):

    def process(self):
        super().process()
        print('Банкомат может осуществлять online-платежи')

    def online(self):
        input('Введите номер карты получателя: ')
        input('Введите сумму платежа: ')


b1 = FirstBankomate('Сбербанк', 100000)
b2 = SecondBankomate('Сбер', 500000)
b2.online()

lst = [b1, b2]

for i in lst:
    i.AboutBankomate()
    i.process()
    i.get_money(1000)
    i.give_money(5000)
