import random


class Employee:
    s = "ABCUDEFO"

    def __init__(self, name=None, surname=None):
        self.name = name if name else self.generate_name()
        self.surname = surname if surname else self.generate_name()
        self.salary = 0

    def say_my_name(self):
        s = f"I'm {self.name} {self.surname}"
        print(s)

    @classmethod
    def generate_name(cls):
        name = ""
        i = 0
        while i < 5:
            name += random.choice(cls.s)
            i += 1
        return name


class RusEmployee(Employee):
    s = "АБВЕОЮИД"


e1 = RusEmployee()
e1.say_my_name()

e2 = Employee()
e2.say_my_name()
