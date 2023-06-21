import random
import time


class Man:
    def __init__(self, name):
        self.name = name

    def solve_task(self):
        print("I'm not ready yet")


class Pupil(Man):
    def __init__(self, name, surname):
        super().__init__(name)
        self.surname = surname

    def solve_task(self):
        time.sleep(random.randint(3, 6))
        super().solve_task()


m = Pupil('Dima', 'Sapegov')
m.solve_task()
