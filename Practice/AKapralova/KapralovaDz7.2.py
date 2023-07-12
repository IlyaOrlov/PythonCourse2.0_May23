import random
import time


class Man:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Привет, меня зовут {self.name}")

    def solve_task(self):
        print("I'm not ready yet")


class Pupil(Man):
    def solve_task(self):
        time.sleep(random.randint(3, 6))
        super().solve_task()


n1 = Man("Аня")
n1.say_hello()
n1.solve_task()
n2 = Pupil("Полина")
n2.say_hello()
n2.solve_task()
