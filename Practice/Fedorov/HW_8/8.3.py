import datetime
import time


class MangerContext:
    new_now = datetime.datetime.now()

    def __enter__(self):
        print(self.new_now)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Зaтраченное время : {datetime.datetime.now() - self.new_now}")


with MangerContext():
    time.sleep(3)
