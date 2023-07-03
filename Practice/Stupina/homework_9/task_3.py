import os
import shutil
import datetime


def show_dir(cur_dir):
    for i in os.listdir(cur_dir):
        path = os.path.join(cur_dir, i)
        d_creation = os.path.getctime(path)
        d_creation = datetime.datetime.fromtimestamp(d_creation)
        d_exist = datetime.datetime.today() - d_creation

        if os.path.isfile(path):
            print(f"Файл: {i}")
            if d_exist > datetime.timedelta(minutes=1):
                os.remove(path)
                print(f'Удалили {i}')
        else:
            print(f"Папка: {i}")
            if os.listdir(path):
                show_dir(path)
            elif d_exist > datetime.timedelta(minutes=2):
                shutil.rmtree(path)
                print(f'Удалили {i}')


s = os.path.join('.', 'my_dir')
while True:
    show_dir(s)
