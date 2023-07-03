import datetime as dt
import time


class MangerContext:

    def __init__(self):
        self.new_now = None

    def __enter__(self):
        self.new_now = dt.datetime.now()
        print(self.new_now)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Зaтраченное время : {dt.datetime.now() - self.new_now}")


with MangerContext():
    time.sleep(3)
