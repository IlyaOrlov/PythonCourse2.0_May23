import shutil
import os


def copydir(source, destination):
    if not os.path.exists(source):
        raise FileNotFoundError(f"Директория {source} не существует.")

    if os.path.exists(destination):
        raise FileExistsError(f"Директория {destination} уже существует.")

    shutil.copytree(source, destination)
    print(f"Директория {source} успешно скопирована в {destination}.")


try:
    copydir("source_dir", "destination_dir")
except FileNotFoundError as e:
    print(e)
except FileExistsError as e:
    print(e)

try:
    copydir("nonexistent_dir", "destination_dir")
except FileNotFoundError as e:
    print(e)
except FileExistsError as e:
    print(e)

try:
    copydir("source_dir", "existing_dir")
except FileNotFoundError as e:
    print(e)
except FileExistsError as e:
    print(e)
