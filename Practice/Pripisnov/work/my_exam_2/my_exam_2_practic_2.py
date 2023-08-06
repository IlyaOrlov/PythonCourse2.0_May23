class Money:
    def __init__(self, rubles, kopeks):
        self.rubles = rubles
        self.kopeks = kopeks

    def __str__(self):
        return f"{self.rubles},{self.kopeks:02d}"

    def __add__(self, other):
        total_rubles = self.rubles + other.rubles
        total_kopeks = self.kopeks + other.kopeks

        if total_kopeks >= 100:
            total_rubles += 1
            total_kopeks -= 100

        return Money(total_rubles, total_kopeks)

    def __sub__(self, other):
        total_rubles = self.rubles - other.rubles
        total_kopeks = self.kopeks - other.kopeks

        if total_kopeks < 0:
            total_rubles -= 1
            total_kopeks += 100

        return Money(total_rubles, total_kopeks)

    def __eq__(self, other):
        return self.rubles == other.rubles and self.kopeks == other.kopeks

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if self.rubles < other.rubles:
            return True
        elif self.rubles == other.rubles and self.kopeks < other.kopeks:
            return True
        else:
            return False

    def __gt__(self, other):
        return not self.__lt__(other) and not self.__eq__(other)

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __ge__(self, other):
        return not self.__lt__(other)


money1 = Money(10, 50)
money2 = Money(5, 75)

total_money = money1 + money2
print(total_money)

diff_money = money1 - money2
print(diff_money)

print(money1 == money2)
print(money1 != money2)
print(money1 < money2)
print(money1 > money2)
print(money1 <= money2)
print(money1 >= money2)
