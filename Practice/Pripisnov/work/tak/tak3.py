class Employee:
    def __init__(self, name, surname, salary):
        self._name = name
        self._surname = surname
        self._salary = salary

    def show(self):                                                                                                                            9
        print(f"{self._name} {self._surname} {self._salary}")


class Manager(Employee)
    def __init__(self,):