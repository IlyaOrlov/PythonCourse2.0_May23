class MainATM:

    def __init__(self, id_atm, balance=0):
        self._id_atm = id_atm
        self._balance = balance

    def View_Balance(self):
        print("******************************************************")
        print(f"Просмотр баланса.ID банкомата:{self._id_atm} Баланс: {self._balance}")

    def Withdraw_Money(self):
        print("******************************************************")
        money = int(input(f"ID банкомата:{self._id_atm} Выбрана операция снятие наличных.\nУкажите сумму, которую хотите снять: "))
        if self._balance > money:
            self._balance -= money
            print(f"Выдача наличных  - {money}")
        else:
            print(f"В банкомате недостаточно ср-в.")

    def Deposit_Money(self):
        print("******************************************************")
        money = int(input(f"ID банкомата:{self._id_atm} Выбрана операция пополнения наличных.\nУкажите сумму, которую хотите внести: "))
        self._balance += money
        print(f"Внесена сумма  - {money}")

    def Inf_ATM(self):
        print("******************************************************")
        print(f"ID банкомата:{self._id_atm}, баланс - {self._balance}.")

    def Inf1_ATM(self):
        print(f"Cписок поддерживаемых операций: \nПросмотр баланса\nВыдача наличных\nПополнение баланса")


class AсceptGiveCash(MainATM):
    pass

class OnlineOperATM(MainATM):

    def Online_Perevod(self):
        print("******************************************************")
        print(f"ID банкомата:{self._id_atm}\nОперация перевод-онлайн.")
        inform = input("Введите номер телефона/карты или счёта получателя: ")
        summa = input("Введите сумму перевода: ")

    def Inf1_ATM(self):
        super().Inf1_ATM()
        print(f"Онлайн-операция.Перевод")

NAMEBANK = "ТСБ"
print(f"Банкоматы {NAMEBANK}:")
ATM1 = AссeptGiveCash("12340", 500000)
#ATM1.Deposit_Money()
ATM2 = AссeptGiveCash("12341", 300000)
#ATM2.View_Balance()
ATM3 = OnlineOperATM("2102314", 1500000)
#ATM3.Online_Perevod()
ATM4 = OnlineOperATM("2102315", 100000)
ATM4.Withdraw_Money()

ATM = {ATM1, ATM2, ATM3, ATM4}
for i in ATM:
    i.Inf_ATM()
    i.Inf1_ATM()
