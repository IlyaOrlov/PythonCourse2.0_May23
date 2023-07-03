import random
import time

class Pupil:
    def solve_task(self):
        delay = random.randint(3, 6)  # Генерируем случайную задержку от 3 до 6 секунд
        time.sleep(delay)
        print("Срабатывание")

# Пример использования
pupil = Pupil()
pupil.solve_task()