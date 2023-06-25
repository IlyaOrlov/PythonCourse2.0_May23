import random

class Employee:
    def __init__(self, name=None, surname=None):
        self.name = name if name else self.generate_name()
        self.surname = surname if surname else self.generate_name()
        self.salary = 0

    def add_salary(self, bonus):
        self.salary += bonus

    def say_my_name(self):
        s = f"I'm {self.name} {self.surname}"
        print(s)

    @staticmethod
    def generate_name():
        s = "ABCUDEFO"
        name = ""
        i = 0
        while i < 5:
            name += random.choice(s)
            i += 1
        return name


e1 = Employee()
e1.say_my_name()
