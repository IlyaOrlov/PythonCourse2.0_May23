# сервер, который создает пользователей банка и начисляет первоначальную сумму, а так же хранит все счета пользователей
class Bank:
    def __init__(self, username, account_numb,  money):
        self._username = username
        self._account_numb = account_numb
        self._money = money

    # Метод пополнения счета
    def replenishment(self, repl):
        self._money += repl

    # Метод снятия денег со счета
    def withdrawal(self, withdrwl):
        self._money -= withdrwl

    # Метод проверяет, одобрено ли снятие денег со счета
    def check_money(self, check):
        if self._money >= check:
            return "YES"
        else:
            return "NO"

    def show_user(self):
        print(f"   NAME: {self._username} | ACCOUNT: {self._account_numb} | money on account: {self._money}$")


# Банкомат для снятия и пополнения наличных
class CashMachine(Bank):
    _cash = 50000

    # Метод, которые принимает наличные деньги с рук, пополняет счет в банке и сохраняет наличку внутри себя
    def replenishment(self):
        coin = int(input("Введите сумму, на которую хотите пополнить счет: "))
        super().replenishment(coin)
        CashMachine._cash += coin
        print(f'Счёт успешно пополнен на {coin}$! | Доступная сумма счета {self._money}$')

    # Метод показывает доступный баланс наличных в банкомате
    @classmethod
    def show_cash(cls):
        print(f'NAME: {cls.__name__} | Balance this machine: {cls._cash}$')

    # Метод, которые снимает деньги со счета и выдает наличные из банкомата
    def withdrawal(self):
        coin = int(input("Введите сумму, которую хотите снять с счета: "))
        c = super().check_money(coin)
        if c == "YES":
            super().withdrawal(coin)
            CashMachine._cash -= coin
            print(f'Сумма {coin}$ успешно снята! | Оставшаяся сумма счета {self._money}$')
        else:
            print(f'/*/==> OperationError: Недостаточно средств на счете!/*/')


# Банкомат для снятия и пополнения наличных, операций с картой, а так же перевода средств между картами клиентов
class CashMachine2(CashMachine):

    def __init__(self, username, account_numb,  money, pin_card):
        super().__init__(username, account_numb,  money)
        self._pin_card = pin_card

    def check_pin(self, pin):
        if self._pin_card == pin:
            return "YES"
        else:
            return "NO"

    # Метод пополняет счет в банке без внесения наличных в банкомат
    def replenishment_card(self):
        pin = int(input("Введите пин-код: "))
        if self.check_pin(pin) == "YES":
            super().replenishment()
        else:
            print('Введен неверный пин-код! Попробуйте снова')

    def withdrawal_card(self):
        pin = int(input("Введите пин-код: "))
        if self.check_pin(pin) == "YES":
            super().withdrawal()
        else:
            print('Введен неверный пин-код! Попробуйте снова')

    def transfer(self, other):
        pin = int(input("Введите пин-код: "))
        self.check_pin(pin)
        coin = int(input('Введите сумму, которую хотите перевести: '))
        c = super().check_money(coin)
        if c == "YES":
            self._money -= coin
            other._money += coin
            print(f'Сумма {coin}$ успешно отправлена! | Оставшаяся сумма счета {self._money}$')
        else:
            print(f'/*/==> OperationError: Недостаточно средств на счете!/*/')




   # Проверка работы классов Bank и CashMachine
# print('#############################')
# bot1 = Bank('Pavel', "#0001", 50000)
# bot1.show_user()
# print('#############################')
# bot2 = CashMachine('Fill', "#0002", 1000)
# bot2.show_user()
# bot2.show_cash()
# print('###########')
# bot2.withdrawal()
# bot2.show_user()
# print('###########')
# bot2.replenishment()
# bot2.show_user()
# print('###########')
# CashMachine.show_cash()

    # Проверка работы класса CashMachine2
# print('#############################')
# bot3 = CashMachine2('Mike', "#0003", 500, 2332)
# bot3.show_user()
# print('###########')
# bot3.withdrawal_card()
# print('###########')
# bot3.replenishment_card()
# bot3.show_user()
# print('###########')
# bot3.replenishment()
# bot3.show_cash()
# print('###########')
# CashMachine2.show_cash()
# print('#############################')


    # Проверка работы класса CashMachine2  на трансфер средств
# bot4 = CashMachine2('Frank', "#0004", 5000, 4455)
# bot5 = CashMachine2('Nick', "#0005", 2000, 3211)
#
# bot4.transfer(bot5)
# bot5.show_user()

