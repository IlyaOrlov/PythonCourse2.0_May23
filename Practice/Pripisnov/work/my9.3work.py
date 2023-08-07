import os
import shutil
import time
from datetime import datetime, timedelta

def delete_old_files_and_folders(folder_path):
    while True:
        for root, dirs, files in os.walk(folder_path, topdown=False):
            for file in files:
                file_path = os.path.join(root, file)
                file_creation_time = os.path.getctime(file_path)
                if datetime.now() - datetime.fromtimestamp(file_creation_time) > timedelta(minutes=1):
                    os.remove(file_path)

            for folder in dirs:
                folder_path = os.path.join(root, folder)
                folder_creation_time = os.path.getctime(folder_path)
                if datetime.now() - datetime.fromtimestamp(folder_creation_time) > timedelta(minutes=2):
                    shutil.rmtree(folder_path)

if __name__ == "__main__":
    path_to_watch = input("Введите путь до папки, за которой следить: ")
    delete_old_files_and_folders(path_to_watch)
