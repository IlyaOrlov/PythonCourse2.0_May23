class ATM:
    def __init__(self, cash_amount):
        self.cash_amount = cash_amount

    def check_balance(self):
        print("Checking balance...")
        print("Available cash:", self.cash_amount)

    def withdraw_cash(self, amount):
        print("Withdrawing cash...")
        if amount <= self.cash_amount:
            self.cash_amount -= amount
            print("Withdrawn:", amount)
            print("Remaining cash:", self.cash_amount)
        else:
            print("Insufficient cash!")

    def deposit_cash(self, amount):
        print("Depositing cash...")
        self.cash_amount += amount
        print("Deposited:", amount)
        print("Total cash:", self.cash_amount)


class OnlineATM(ATM):
    def __init__(self, cash_amount):
        super().__init__(cash_amount)

    def make_payment(self, amount):
        print("Making online payment...")
        if amount <= self.cash_amount:
            self.cash_amount -= amount
            print("Payment successful!")
            print("Remaining cash:", self.cash_amount)
        else:
            print("Insufficient cash for payment!")


# Тестирование системы
atms = [
    ATM(10000),
    OnlineATM(5000),
    ATM(20000)
]

for atm in atms:
    print("--- ATM Information ---")
    atm.check_balance()
    atm.withdraw_cash(3000)
    atm.deposit_cash(2000)
    if isinstance(atm, OnlineATM):
        atm.make_payment(1500)
    print("-----------------------")
