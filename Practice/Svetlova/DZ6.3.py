import tempfile
import os

class WrapStrToFile:
    def __init__(self):
        self._file_path = tempfile.mktemp()

    @property
    def content(self):
        try:
            with open(self._file_path, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return 'Файл еще не существует'

    @content.setter
    def content(self, value):
        with open(self._file_path, 'w') as file:
            file.write(value)

    @content.deleter
    def content(self):
        if os.path.exists(self._file_path):
            os.remove(self._file_path)

wrap = WrapStrToFile()
print(wrap.content)  # Вывод: Файл еще не существует

wrap.content = 'Привет, мир!'
print(wrap.content)  # Вывод: Привет, мир!

del wrap.content
print(wrap.content)  # Вывод: Файл еще не существует