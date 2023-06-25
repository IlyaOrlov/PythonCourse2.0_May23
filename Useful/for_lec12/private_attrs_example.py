class Employee:
    def __init__(self, name, surname, salary):
        self.__name = name  # self._Employee__name
        self.__surname = surname  # self._Employee__surname
        self.__salary = salary  # self._Employee__salary

    def say_my_name(self):
        print(self.__name)


class Manager(Employee):
    def __init__(self, name, surname, salary):
        super().__init__(name, surname, salary)

    def say_my_name(self):
        print(self.__name)  # self._Manager__name


e1 = Employee("Ivan", "Ivanov", 200000)
m1 = Manager("Petr", "Petrov", 250000)
m1.say_my_name()