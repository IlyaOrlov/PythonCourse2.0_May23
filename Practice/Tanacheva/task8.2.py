import time
import random


class Man:

    def __init__(self, name):
        self.name = name

    def solve_task(self):
        print("I'm not ready yet")


class Pupil(Man):

    def solve_task(self):
        t = random.randint(3, 6)
        time.sleep(t)
        super().solve_task()


p1 = Pupil("Tom")
print(p1)
p1.solve_task()
