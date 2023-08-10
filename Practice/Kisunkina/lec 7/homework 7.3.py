# Реализовать систему, эмулирующую работу с банкоматами. Создать семейство классов банкоматов,
# хранящих определенные суммы и поддерживающих различные операции (одни банкоматы принимают и выдают
# наличные, другие позволяют еще и проводить онлайн платежи). Операции реализуются посредством методов,
# выводящих название операции и меняющих (при необходимости) количество наличных в банкомате. Для
# тестирования системы необходимо реализовать алгоритм, обходящий список банкоматов разного типа и
# запрашивающий у каждого банкомата информацию о количестве наличных и наборе поддерживаемых операций.

class ATM:
    def __init__(self, balance):
        self.balance = float(balance)

    def about_atm(self):
        print("Банкомат может выдавать и принимать наличные")

    def give_money(self, money):
        if self.balance > money:
            self.balance -= money
            print(f"На Вашем счету осталось: {self.balance} рублей")
        else:
            print("На счете недостаточно средств!")

    def take_money(self, money):
        self.balance += money
        print (f"На Вашем счету теперь: {self.balance} рублей")


class FirstAtm(ATM):
    def __init__(self, balance):
        super().__init__(balance)
        self.name = "Счёт № 1"


class SecondAtm(ATM):
    def __init__(self, balance):
        super().__init__(balance)
        self.name = "Счёт № 2"

    def about_atm(self):
        super().about_atm()
        print("Банкомат может осуществлять online платежи")

    def online(self, money):
        input("Введите номер получателя средств: ")
        self.give_money(money)



atm1 = FirstAtm(100000)
atm2 = SecondAtm(50000)

atm = [atm1, atm2]

for i in atm:
    print(f"Вы снимаете деньги с {i.name}")
    money = int(input("Ведите сумму, которую хотите снять: "))
    i.give_money(money)
    money = int(input("Ведите сумму, которую хотите положить на счёт: "))
    i.take_money(money)
    if isinstance(i, SecondAtm):
        money = int(input("Ведите сумму, которую хотите перевести: "))
        i.online(money)
