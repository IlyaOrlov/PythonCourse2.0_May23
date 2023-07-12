class ATM:
    def __init__(self, cash):
        self.cash = cash

    def withdraw_cash(self, amount):
        if amount <= self.cash:
            self.cash -= amount
            print(f"Снял {amount} наличными.")
        else:
            print("Недостаточно наличных средств.")

    def deposit_cash(self, amount):
        self.cash += amount
        print(f"Внесенная {amount} наличными.")


class OnlineATM(ATM):
    def make_online_payment(self, amount):
        if amount <= self.cash:
            self.cash -= amount
            print(f"Произвел онлайн-платеж в размере {amount}.")
        else:
            print("Недостаточно наличных для онлайн-оплаты")


def main():
    atm1 = ATM(1000)
    atm2 = OnlineATM(2000)
    atm3 = ATM(500)

    atm_list = [atm1, atm2, atm3]

    for atm in atm_list:
        print(f"ATM Тип: {type(atm).__name__}")
        print(f"Доступные наличные: {atm.cash}")

        if isinstance(atm, OnlineATM):
            atm.make_online_payment(500)

        atm.withdraw_cash(200)
        atm.deposit_cash(300)

        print(f"Доступные деньги: {atm.cash}")
        print()


if __name__ == "__main__":
    main()