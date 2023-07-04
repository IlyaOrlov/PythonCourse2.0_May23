class ATM:
    def __init__(self, name, balance=0):
        self._name = name
        self._balance = float(balance)

    def about_atm(self):
        print(f"Банкомат: {self._name} Баланс: {self._balance}")


class GetATM(ATM):
    @staticmethod
    def get_operation():
        print("Банкомат может осуществлять операцию получения наличных.")

    def get_money(self, money):
        self._balance += money


class GiveATM(ATM):
    @staticmethod
    def give_operation():
        print("Банкомат может осуществлять операцию выдачи наличных.")

    def give_money(self, money):
        if self._balance - money < 0:
            print(f"В Банкомате:{self._name} недостаточно денежных средств.")
        else:
            self._balance -= money


class OnlineATM(ATM):
    @staticmethod
    def online_operation():
        print("Банкомат может осуществлять только онлайн операции.")

    def online_payment(self):
        print(f'{self._name}: Совершен онлайн-платеж')


b1 = GetATM("Сбер", 0)
b1.about_atm()
b1.get_operation()
b1.get_money(200)
b1.about_atm()

b2 = GiveATM("Альфа", 1000)
b2.about_atm()
b2.give_operation()
b2.give_money(100)
b2.about_atm()

b3 = OnlineATM("ВТБ", 0)
b3.about_atm()
b3.online_operation()
b3.online_payment()
b3.about_atm()

# lst = [b1, b2, b3]
# for i in lst:
#     i.about_atm()