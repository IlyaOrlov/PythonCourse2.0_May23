import time

class ExecutionTimer:
    def __enter__(self):
        self.start_time = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        end_time = time.time()
        print(f"Execution time: {end_time - self.start_time} seconds")

# Пример использования

with ExecutionTimer():
    # Код, время исполнения которого нужно замерить
    number_list = range(1000000)
    squared_list = [x**2 for x in number_list]