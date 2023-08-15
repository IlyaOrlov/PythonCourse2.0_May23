class IncorrectDataInput(Exception):
    pass


class Money:
    def __init__(self, x, y):
        if isinstance(x, int) and isinstance(y, int):
            if x >= 0 and 0 <= y < 100:
                self.__x = x
                self.__y = y
                self._money = float(f'{self.__x}.{self.__y}')
            else:
                raise IncorrectDataInput
        else:
            print('Некорректный тип атрибутов')
    @property
    def money(self):
       return self._money

    def __str__(self):
        return f'{self.__x},{self.__y}'

    def __add__(self, other):
        res = round(self._money + other._money, 2)
        res = str(res).split('.')
        return Money(int(res[0]), int(res[1]))

    def __sub__(self, other):

        res = round(self._money - other._money, 2)
        if res < 0:
            print('Денежная сумма не может быть отрицательной')
            return None
        else:
            res = str(res).split('.')
            return Money(int(res[0]), int(res[1]))

    def __lt__(self, other):
        return self._money < other._money

    def __eq__(self, other):
        return self._money == other._money

    def __le__(self, other):
        return self._money <= other._money


if __name__ == '__main__':
    ob1 = Money(10, 20)
    ob2 = Money(10, 4)

    print(ob1, ob2)
    print(ob1 - ob2)
    print(ob1 >= ob2)
