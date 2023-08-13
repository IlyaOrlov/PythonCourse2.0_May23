class Atm:
    def __init__(self, number, balance=0):
        self._number = number
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @staticmethod
    def online_pay():
        pass

    def about(self):
        print(f"Банкомат номер: {self._number} баланс: {self._balance}")
        print("Банкомат может осуществлять следующие операции:\n"
              "get_cash - получение наличных\n"
              "give_cash - выдача наличных")

    def get_cash(self, cash):
        self._balance += cash
        print(f"Было осуществленно получение наличных (get_cash), баланс: {self._balance}")

    def give_cash(self, cash):
        if self._balance - cash < 0:
            print(f"Недостаточно денежных средств.")
        else:
            self._balance -= cash
            print(f"Была осуществленна выдача наличных (give_cash), баланс: {self._balance}")


class AtmV1(Atm):
    pass


class AtmV2(Atm):
    @staticmethod
    def online_pay():
        input("Введите номер карты получателя ")
        input("Введите сумму ")

    def about(self):
        super().about()
        print("online_pay - оплата онлайн")


atm1 = Atm('1010023',10000)
atm2 = AtmV1('1010024',15000)
atm3 = AtmV2('1010025',25000)
lst = [atm1, atm2, atm3]

for i in lst:
    i.about()
    i.get_cash(1000)
    i.give_cash(13000)
    i.online_pay()
