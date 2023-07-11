#Написать класс Man, который принимает имя в конструкторе. Имеет метод solve_task, который просто выводит
#"I'm not ready yet".
class Man:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def solve_task():
        print("I'm not ready yet")


m1 = Man("Иван")
m1.solve_task()
