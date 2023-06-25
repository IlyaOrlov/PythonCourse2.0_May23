# * Реализовать систему, эмулирующую работу с банкоматами.
# Создать семейство классов банкоматов, хранящих определенные суммы и поддерживающих различные операции
# (одни банкоматы принимают и выдают наличные, другие позволяют еще и проводить онлайн платежи).
# Операции реализуются посредством методов, выводящих название операции и меняющих (при необходимости)
# количество наличных в банкомате. Для тестирования системы необходимо реализовать алгоритм, обходящий
# список банкоматов разного типа и запрашивающий у каждого банкомата информацию о количестве наличных
# и наборе поддерживаемых операций.

class ATM:
    def __init__(self, name, balance=0):
        self.name = name
        self._balance = float(balance)

    def about_atm(self):
        print(f"Банкомат: {self.name} Баланс: {self.balance}")
        print("Банкомат может осуществлять следующие операции:\n"
              "get_money - получение банкоматом наличных\n"
              "give_money - выдача банкоматом наличных")
        
    def get_money(self, money):
        self._balance += money

    def give_money(self, money):
        if self._balance - money < 0:
            print(f"В Банкомате:{self.name} недостаточно денежных средств.")
        else:
            self._balance -= money


class BaseATM(ATM):
    pass


class NewATM(ATM):
    
    def online_payment(self):
        print("Создание онлайн платежа")

    def about_atm(self):
        super().about_atm()
        print("online_payments - онлайн платежи")


b = BaseATM("aaa", 200)
b1 = ATM("bbb", 0)
b2 = NewATM("ccc", 1000)

lst = [b, b1, b2]

for i in lst:
    i.give_money(200)
    i.about_atm()
