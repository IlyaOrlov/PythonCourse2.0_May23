class Employee:
    def __init__(self, name=None, surname=None, salary=0):
        self.name = name
        self.surname = surname
        self._salary = salary
        self._bonus = 0

    @property  # гЕттер
    def money(self):
        return self._salary + self._bonus

    @money.setter  # сЕттер
    def money(self, bonus):
        if isinstance(bonus, int):
            self._bonus += bonus
        else:
            print("Incorrect type!")

    def say_my_name(self):
        print(f"I'm {self.name} {self.surname} salary={self._salary}")

    def __gt__(self, other):
        return self._salary > other.salary


e1 = Employee("Ivan", "Ivanov", 100000)
print(e1.money)
e1.money = "1000"
e1.money = 50000
print(e1.money)
