import time
import random


class Man:
    def __init__(self, name):
        self.name = name


    @staticmethod
    def solve_task():
        print("I'm not ready yet")


class Pupil(Man):
    def solve_task(self):
        time.sleep(random.randint(3, 6))
        super().solve_task()


human = Pupil('Людмила')
human.solve_task()