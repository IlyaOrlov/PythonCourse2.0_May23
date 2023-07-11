class Employee:
    def __init__(self, name=None, surname=None, salary=0):
        self.name = name
        self.surname = surname
        self.salary = salary

    def add_salary(self, bonus):
        self.salary += bonus

    def say_my_name(self):
        print(f"I'm {self.name} {self.surname} salary={self.salary}")

    def __gt__(self, other):
        return self.salary > other.salary

    def __ge__(self, other):
        return self.salary >= other.salary

    def __eq__(self, other):
        return self.name == other.name \
            and self.surname == other.surname\
            and self.salary == other.salary


e1 = Employee("Ivan", "Ivanov", 100000)
e2 = Employee("Ivan", "Ivanov", 100000)
print(e2 <= e1)
print(e2 == e1)
