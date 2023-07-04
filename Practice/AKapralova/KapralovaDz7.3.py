class ATM:
    def __init__(self, name, balance=0):
        self._name = name
        self._balance = float(balance)

    def about_atm(self):
        print(f"Банкомат: {self._name} Баланс: {self._balance}")

    def get_money(self, money):
        self._balance += money

    def give_money(self, money):
        if self._balance - money < 0:
            print(f"В Банкомате:{self._name} недостаточно денежных средств.")
        else:
            self._balance -= money


class GetGiveATM(ATM):
    @staticmethod
    def operation():
        print("Банкомат может осуществлять операцию получения и выдачи наличных.")


class OnlineATM(ATM):
    @staticmethod
    def online_operation():
        print("Банкомат может осуществлять операцию получения и выдачи наличных, а так же онлайн платежи")

    def online_payment(self):
        print(f'{self._name}: Совершен онлайн платеж')


b1 = GetGiveATM("Сбер", 1000)
b1.operation()

b2 = OnlineATM("ВТБ", 2000)
b2.online_operation()
b2.online_payment()

lst = [b1, b2]
for i in lst:
    i.get_money(100)
    i.give_money(200)
    i.about_atm()
