class Employee:
    name = "_"
    surname = "_"
    salary = 0

    def __init__(self, name_, surname_, surname2_=''):
        self.name = name_
        self.surname = surname_
        self.surname2 = surname2_
        self.salary = 0

    def add_salary(self, bonus):
        self.salary += bonus

    def say_my_name(self):
        s = f"I'm {self.name} {self.surname}"
        if self.surname2:
            s = f"{s}-{self.surname2}"
        print(s)


e1 = Employee("Ivan", "Ivanov")
e1.add_salary(10000)  # Employee.add_salary(e1, 10000)

e2 = Employee("Petr", "Petrov")
e2.surname2 = "Vodkin"
e2.add_salary(20000)

e1.say_my_name()
print(f"{e1.salary=}")
print("#####################")
e2.say_my_name()
print(f"{e2.salary=}")
print("#####################")
print(f"{Employee.name=}")
print(f"{Employee.surname=}")



