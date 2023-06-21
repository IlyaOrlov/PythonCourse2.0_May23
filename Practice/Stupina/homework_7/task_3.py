class ATM:
    operations = ['снятие наличных', 'внесение наличных', 'баланс', 'онлайн-платеж']
    __num = 0

    def __init__(self, summa, bank):
        self.__summa = summa
        self.bank = bank
        self.name = self.__generator_name()

    @classmethod
    def __generator_name(cls):
        cls.__num += 1
        return f'{cls.__name__}-{cls.__num}'

    def cash_in(self, value):
        self.__summa += value
        print(f'{self.name}: Вы положили на счет: {value}')

    def cash_out(self, value):
        if self.__summa > value:
            self.__summa -= value
            print(f'{self.name}: Выдача наличных: {value}')
        else:
            print('Неудачная попытка снятия: В банкомате недостаточно средств!')

    def balance(self):
        print(f'Остаток {self.name}: {self.__summa}')

    def info_operations(self):
        print(f'\nДоступные операции банкомата {self.name}: {self.operations}')

    def info_num(self):
        print(f'Всего банкоматов типа {type(self).__name__} - {self.__num} шт.')

    @staticmethod
    def info_bank(lst_ob):
        print('\n------ Информация по банкам ------')
        d = {}
        for i in lst_ob:
            if i.bank in d:
                d[i.bank] += 1
            else:
                d[i.bank] = 1

        for i in d:
            b = {}
            for j in lst_ob:
                if j.bank == i:
                    if type(j).__name__ in b:
                        b[type(j).__name__] += 1
                    else:
                        b[type(j).__name__] = 1

            print(f'Всего банкоматов банка {i} - {d[i]} шт:')
            for j in b:
                print(f' - банкоматы типа {j} - {b[j]} шт')

    def test(self):
        self.info_operations()
        self.balance()

    def payments(self):
        raise NotImplementedError


class ATMCashInOut(ATM):
    operations = ATM.operations[0:3]


class ATMPayments(ATM):
    def payments(self):
        print(f'{self.name}: Совершен онлайн-платеж')


atm_1 = ATMCashInOut(100000, 'Sber')
atm_1.cash_out(500000)

atm_2 = ATMPayments(100000, 'Tinkoff')
atm_2.cash_in(3000)

atm_3 = ATMPayments(200000, 'Sber')
atm_2.payments()

atm_4 = ATMCashInOut(100000, 'Alfa')

atm = {atm_1, atm_2, atm_3, atm_4}

for t in atm:
    t.test()

ATM.info_bank(atm)
