class NoDataError(Exception):
    pass


fname = input('Введите имя файла: ')
try:
    f = open(fname)
    data = f.read()
    if data:
        print(data)
    else:
        raise NoDataError("Нет данных")
    f.close()
except FileNotFoundError as ex:
    print(f"Ошибка. Файл не существует: {ex}")
except NoDataError as ex:
    print(f"Ошибка. В файле нет данных: {ex}")

print("Продолжаем работу...")