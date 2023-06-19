import random
import time


class Man:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def solve_task():
        print("I'm not ready yet")


class Pupil(Man):
    def __init__(self, name, surname):
        super().__init__(name)
        self.surname = surname

    @staticmethod
    def solve_task():
        time.sleep(random.randint(3, 6))


m = Pupil('Dima', 'Sapegov')
m.solve_task()
