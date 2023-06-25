class ATM:
    _operations = 'снятие наличных', 'внесение наличных', 'баланс', 'онлайн-платеж'
    __num = 0

    def __init__(self, summa, bank):
        self.__summa = summa
        self._bank = bank
        self._name = self.__generator_name()

    @property
    def name(self):
        return self._name

    @property
    def bank(self):
        return self._bank

    @name.setter
    def name(self, *args):
        print('Имя банкомата не может быть изменено!')

    @bank.setter
    def bank(self, x):
        if input('Вы действительно хотите поменять банк? Введите да/нет:').lower() == 'да':
            self._bank = x
            print(f'Банк банкомата {self._name} был изменен')

    @classmethod
    def __generator_name(cls):
        cls.__num += 1
        return f'{cls.__name__}-{cls.__num}'

    def cash_in(self, value):
        self.__summa += value
        print(f'{self._name}: Вы положили на счет: {value}')

    def cash_out(self, value):
        if self.__summa > value:
            self.__summa -= value
            print(f'{self._name}: Выдача наличных: {value}')
        else:
            print('Неудачная попытка снятия: В банкомате недостаточно средств!')

    def balance(self):
        print(f'Остаток {self._name}: {self.__summa}')

    def info_operations(self):
        print(f'\nДоступные операции банкомата {self._name}: {self._operations}')

    def info_num(self):
        print(f'Всего банкоматов типа {type(self).__name__} - {self.__num} шт.')

    @staticmethod
    def info_bank(set_ob):
        print('\n------ Информация по банкам ------')
        d = {}
        set_atm = set()
        for i in set_ob:
            set_atm.add(type(i).__name__)
            if i.bank in d:
                b = d[i.bank]
                if type(i).__name__ in b:
                    b[type(i).__name__] += 1
                else:
                    b[type(i).__name__] = 1
            else:
                d[i.bank] = {type(i).__name__: 1}

        for i in d:
            n = 0
            s = ''
            for j in set_atm:
                n += d[i].get(j, 0)
                s = s + f'\n  - {j}: {d[i].get(j,0)} шт'
            print(f'Банкоматы банка {i} - {n} шт:{s}')

    def test(self):
        self.info_operations()
        self.balance()

    def payments(self):
        raise NotImplementedError


class ATMCashInOut(ATM):
    _operations = ATM._operations[0:3]


class ATMPayments(ATM):
    def payments(self):
        print(f'{self._name}: Совершен онлайн-платеж')


atm_1 = ATMCashInOut(600000, 'Sber')
atm_1.cash_out(500000)

atm_2 = ATMPayments(200000, 'Sber')
atm_2.cash_in(3000)
atm_2.payments()

atm_3 = ATMPayments(500000, 'Sber')
atm_4 = ATMCashInOut(100000, 'Alfa')
atm_5 = ATMPayments(400000, 'Tinkoff')

atm = {atm_1, atm_2, atm_3, atm_4, atm_5}

ATM.info_bank(atm)
[t.test() for t in atm]

atm_1.bank = 'fgdf'
print(atm_1.bank)
