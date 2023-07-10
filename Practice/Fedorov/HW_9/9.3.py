import os
import datetime as dt


def difference_time(path, minut):
    return (dt.datetime.now() - dt.datetime.fromtimestamp(os.path.getctime(path)) > dt.timedelta(minutes=minut))


tfs_path = input("Введите путь")
while True:
    for root, dirs, files in os.walk(tfs_path):
        for file in files:
            file_path = root + f"\\{file}"
            if difference_time(file_path, 1):
                try:
                    os.remove(file_path)
                except OSError:
                    print(f"Файл:\n{file_path}\n- не может быть удален")
        for folder in dirs:
            folder_path = root + f"\\{folder}"
            if difference_time(folder_path, 2):
                try:
                    os.rmdir(folder_path)
                except OSError:
                    print(f"Папка:\n{folder_path}\n- не может быть удалена")
