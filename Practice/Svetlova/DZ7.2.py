import time
from random import randint

class Man:
    def __init__(self, name):
        self.name = name

    def solve_task(self):
        print("Я еще не готов")

class Pupil(Man):
    def solve_task(self):
        thinking_time = randint(3, 6)
        print(f"{self.name} размышляет...")
        time.sleep(thinking_time)
        print(f"{self.name} решил/а задачу")

# Пример использования классов
man = Man("Джон")
man.solve_task()  # Вывод: "Я еще не готов"

pupil = Pupil("Алиса")
pupil.solve_task()
# Вывод:
# "Алиса размышляет..."
# [ожидание случайного времени от 3 до 6 секунд]
# "Алиса решила задачу"