class Employee:
    def __init__(self, name=None, surname=None, salary=0):
        self.name = name
        self.surname = surname
        self.salary = salary

    def add_salary(self, bonus):
        self.salary += bonus

    def say_my_name(self):
        print(f"I'm {self.name} {self.surname} {self.salary}")

    def __gt__(self, other):
        return self.salary >= other.salary

    def __ge__(self, other):
        return self.salary > other.salary

    def __eq__(self, other):
        return self.salary > other.salary
