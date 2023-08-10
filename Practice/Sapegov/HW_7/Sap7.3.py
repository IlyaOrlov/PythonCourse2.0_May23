class Atms:

    def __init__(self, nomber, cash):
        self._nomber = nomber
        self._cash = cash

    def status(self):
        print(f'Банкомат номер {self._nomber}, количество наличных: {self._cash} руб.')

    def replenishment(self, change):
        self._cash += change
        print(f'На счет банкомата {self._nomber} внесено {change} руб.')

    def withdrawal(self, change):
        if self._cash >= change:
            self._cash -= change
            print(f'Со счета банкомата {self._nomber} списано {change} руб.')
        else:
            print(f'На счете банкомата {self._nomber} недостаточно средств')


class AtmSimple(Atms):
    pass


class AtmOnline(Atms):

    def online_pay(self):
        recipient = input('Введите счет, либо телефон получателя: ')
        change = int(input('Введите сумму для перевода: '))
        super().withdrawal(change)
        if self._cash >= change:
            print(f'Вы совершили онлайн перевод на счет {recipient}')


atm1 = AtmSimple('№111', 10000)
atm2 = AtmSimple('№222', 50000)
atm3 = AtmOnline('№333', 20000)
atms = (atm1, atm2, atm3)

atm1.replenishment(5500)
atm2.withdrawal(500)
atm3.online_pay()

for i in atms:
    i.status()
