class Employee:
    state = "RF"

    def __init__(self, name, surname, salary):
        self._name = name
        self._surname = surname
        self._salary = salary

    def add_salary(self, bonus):
        self._salary += bonus

    def __str__(self):
        return f"{self._name} {self._surname} with salary={self._salary}"


class Manager(Employee):
    def __init__(self, name, surname, salary):
        super().__init__(name, surname, salary)

    def add_salary(self, bonus):
        self._salary += bonus * 2

    def __str__(self):
        return f"Manager {self._name} {self._surname} with salary={self._salary}"


lst = [Manager("Ivan", "Ivanov", 200000), Employee("Petr", "Petrov", 250000)]
for emp in lst:
    print(emp)
    emp.add_salary(50000)
    print(emp)
