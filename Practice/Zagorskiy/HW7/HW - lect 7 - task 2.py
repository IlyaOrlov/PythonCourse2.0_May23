# Написать класс Pupil, у которого переопределен метод solve_task. На этот раз он будет думать от 3 до 6 секунд
# (c помощью метода sleep библиотеки time и randint библиотеки random).
from time import sleep
from random import randint


class Man:
    def __init__(self, name):
        self.name = name

    def solve_task(self):
        print("I'm not ready yet")


class Pupil(Man):
    def __init__(self, name):
        super().__init__(name)

    def solve_task(self):
        sleep(randint(3, 6))
        super().solve_task()


bot = Pupil('Pavel')
bot.solve_task()
