import os
import shutil
import time


folder_path = input("Укажите полный путь до папки: ")
while True:
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_age = time.time() - os.path.getctime(file_path)
            if file_age > 60:
                os.remove(file_path)
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            dir_age = time.time() - os.path.getctime(dir_path)
            if dir_age > 120:
                shutil.rmtree(dir_path)
    time.sleep(10)
