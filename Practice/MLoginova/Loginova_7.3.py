class MainATM:
    __NAME_BANK = "ТСБ"

    def __init__(self, id_atm, balance=0):
        self._id_atm = id_atm
        self._balance = balance

    def withdraw_money(self):
        print("******************************************************")
        money = int(input(f"{self.__NAME_BANK} ID банкомата:{self._id_atm} Выбрана операция снятие наличных."
                          f"\nУкажите сумму, которую хотите снять: "))
        if self._balance > money:
            self._balance -= money
            print(f"Выдача наличных  - {money}")
        else:
            print(f"В банкомате недостаточно ср-в.")

    def deposit_money(self):
        print("******************************************************")
        money = int(input(f"{self.__NAME_BANK} ID банкомата:{self._id_atm} Выбрана операция пополнения наличных."
                          f"\nУкажите сумму, которую хотите внести: "))
        self._balance += money
        print(f"Внесена сумма  - {money}")

    def inf_balance(self):
        print("******************************************************")
        print(f"{self.__NAME_BANK} ID банкомата:{self._id_atm}, баланс - {self._balance}.")

    @staticmethod
    def list_operation():
        print(f"Cписок поддерживаемых операций: \nПросмотр баланса\nВыдача наличных\nПополнение баланса")


class AcceptGiveCash(MainATM):
    pass


class OnlineOperATM(MainATM):

    def online_perevod(self):
        print("******************************************************")
        print(f"{self.__NAME_BANK} ID банкомата:{self._id_atm}\nОперация перевод-онлайн.")
        inform = input("Введите номер телефона/карты или счёта получателя: ")
        summa = input("Введите сумму перевода: ")
        return inform, summa

    def list_operation(self):
        super().list_operation()
        print(f"Онлайн-операция.Перевод")


ATM1 = AcceptGiveCash("12340", 500000)
#ATM1.deposit_money()
ATM2 = AcceptGiveCash("12341", 300000)
#ATM2.inf_balance()
ATM3 = OnlineOperATM("2102314", 1500000)
#ATM3.online_perevod()
ATM4 = OnlineOperATM("2102315", 100000)
ATM4.withdraw_money()

ATM = {ATM1, ATM2, ATM3, ATM4}
for i in ATM:
    i.inf_balance()
    i.list_operation()
