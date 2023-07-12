import os
import tempfile


class WrapStrToFile:

    def __init__(self):
        # здесь инициализируется атрибут filepath, он содержит путь до файла-хранилища
        self._filepath = tempfile.mktemp()

    @property
    def content(self):
        # попытка чтения из файла, в случае успеха возвращаем содержимое
        # в случае неудачи возвращаем 'File doesn't exist'
        try:
            with open(self._filepath, "r") as f:
                res = f.read()
            return res
        except:
            return "Файл еще не существует"

    @content.setter
    def content(self, value):
        # попытка записи в файл указанного содержимого
        with open(self._filepath, "w") as f:
            f.write(value)

    @content.deleter
    def content(self):
        # удаляем файл: os.remove(имя_файла)
        os.remove(self._filepath)


wstf = WrapStrToFile()
print(wstf.content)  # Output: File doesn't exist
wstf.content = 'test str'
print(wstf.content)  # Output: test_str
wstf.content = 'text 2'
print(wstf.content)  # Output: text 2
del wstf.content  # после этого файла не существует
