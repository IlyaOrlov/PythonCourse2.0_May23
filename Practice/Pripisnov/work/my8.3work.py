import time


class ExecutionTimer:
    def __enter__(self):
        self.start_time = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed_time = time.time() - self.start_time
        print(f"Execution time: {elapsed_time} seconds")


# Пример использования менеджера контекста
with ExecutionTimer():
    # Код, исполнение которого нужно замерить
    for i in range(1000000):
        pass
