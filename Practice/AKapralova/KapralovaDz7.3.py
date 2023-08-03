class ATM:
    def __init__(self, name, balance=0):
        self._name = name
        self._balance = float(balance)

    def about_atm(self):
        print(f"Банкомат: {self._name} Баланс: {self._balance}")

    def operation(self):
        print("Банкомат может осуществлять операции получения и выдачи наличных.")

    def get_money(self, money):
        self._balance += money

    def give_money(self, money):
        if self._balance - money < 0:
            print(f"В Банкомате:{self._name} недостаточно денежных средств.")
        else:
            self._balance -= money


class GetGiveATM(ATM):
    pass


class OnlineATM(ATM):
    def operation(self):
        super().operation()
        print("Банкомат может осуществлять онлайн платежи.")

    def online_payment(self):
        print(f'{self._name}: Совершен онлайн платеж')


b1 = GetGiveATM("Сбер", 1000)

b2 = OnlineATM("ВТБ", 2000)
b2.online_payment()

lst = [b1, b2]
for i in lst:
    i.about_atm()
    i.operation()
    i.get_money(100)
    i.give_money(200)
