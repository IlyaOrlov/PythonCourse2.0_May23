class Employee:
    def __init__(self, name=None, surname=None, salary=0):
        self.name = name
        self.surname = surname
        self.salary = salary

    def say_my_name(self):
        print(f"I'm {self.name} {self.surname} salary={self.salary}")

    def __repr__(self):
        return f"{self.surname} {self.name}"

    def __lt__(self, other):
        if self.surname == other.surname:
            return self.name < other.name
        else:
            return self.surname < other.surname


e1 = Employee("Ivan", "Ivanov", 100000)
e2 = Employee("Petr", "Petrov", 200000)
e3 = Employee("Alexandr", "Ivanov", 150000)
lst = [e1, e2, e3]
lst.sort()
print(lst)

lst.sort(key=lambda el: el.salary)
print(lst)