import os


def copyfile(source, destination):
    if not os.path.exists(source):
        raise FileNotFoundError(f"Файл {source} не найден.")
    if not os.access(source, os.R_OK):
        raise PermissionError(f"Нет доступа к файлу {source}.")

    if os.path.exists(destination):
        raise FileExistsError(f"Файл {destination} уже существует.")

    try:
        with open(source, 'rb') as source_file:
            file_content = source_file.read()

        with open(destination, 'wb') as destination_file:
            destination_file.write(file_content)

        print(f"Файл {source} успешно скопирован в {destination}.")
    except Exception as e:
        print(f"Произошла ошибка при копировании файла: {str(e)}")


# Примеры использования
try:
    copyfile('source.txt', 'destination.txt')
except Exception as e:
    print(str(e))

try:
    copyfile('nonexistent.txt', 'destination.txt')
except Exception as e:
    print(str(e))

try:
    copyfile('protected.txt', 'destination.txt')
except Exception as e:
    print(str(e))

try:
    copyfile('source.txt', 'existing.txt')
except Exception as e:
    print(str(e))
