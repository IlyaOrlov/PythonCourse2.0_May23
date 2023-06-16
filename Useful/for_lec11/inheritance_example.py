class Employee:
    def __init__(self, name, surname, salary):
        self._name = name
        self._surname = surname
        self._salary = salary

    def show(self):
        print(f"{self._name} {self._surname} {self._salary}")


class Manager(Employee):
    def __init__(self, name, surname, salary, employees):
        super().__init__(name, surname, salary)
        self._employees = employees


e1 = Employee("Ivan", "Ivanov", 100000)
m1 = Manager("Petr", "Petrov", 1500000, (e1,))
lst = [e1, m1]
for i in lst:
    i.show()
