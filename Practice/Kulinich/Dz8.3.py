import time


class CtxMngTimer:
    def __enter__(self):
        self.start_time = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        end_time = time.time() - self.start_time
        print(f"Время выполнения операции: {end_time} секунд")


word = "Бинго"
with CtxMngTimer():
    with open("D:/123.txt", "w") as dok:
        dok.write(word)