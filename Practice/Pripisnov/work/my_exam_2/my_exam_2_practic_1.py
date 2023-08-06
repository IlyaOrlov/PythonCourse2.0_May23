class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setAge(self, age):
        self.age = age

    def getAge(self):
        return self.age


class Worker(User):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def setSalary(self, salary):
        self.salary = salary

    def getSalary(self):
        return self.salary


# Создание объекта John
john = Worker('John', 25, 1000)

# Создание объекта Jack
jack = Worker('Jack', 26, 2000)

# Нахождение суммы зарплат объектов John и Jack
total_salary = john.getSalary() + jack.getSalary()

print("Сумма зарплат John и Jack:", total_salary)
