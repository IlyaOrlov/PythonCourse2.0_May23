#Написать класс Pupil, у которого переопределен метод solve_task. На этот раз он будет думать от 3 до 6 секунд
#(c помощью метода sleep библиотеки time и randint библиотеки random).
import time
import random


class Man:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def solve_task():
        print("I'm not ready yet")

class Pupil(Man):
    @staticmethod
    def solve_task():
        super().solve_task()
        time.sleep(random.randint(3, 6))


m1 = Man("Aleksey")
m1.solve_task()
print("###################")
m2 = Man("Sergey")
m2.solve_task()
