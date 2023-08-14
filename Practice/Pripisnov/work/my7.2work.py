import time
from random import randint

class Pupil:
    def solve_task(self):
        thinking_time = randint(3, 6)  # Генерация случайного времени от 3 до 6 секунд
        time.sleep(thinking_time)  # Задержка выполнения программы на указанное количество секунд
        print("I'm ready now!")


# Пример использования класса
pupil = Pupil()
pupil.solve_task()
