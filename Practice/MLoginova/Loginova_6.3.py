import tempfile
import os


class WrapStrToFile:

    def __init__(self):
    #здесь инициализируется атрибут filepath, он содержит путь до файла-хранилища
        self.filepath = tempfile.mktemp()
    @property
    def content(self):
        try:
            # попытка чтения из файла, в случае успеха возвращаем содержимое
            with open(self.filepath) as f:
                return f.read()
        except FileNotFoundError:
            # в случае неудачи возвращаем 'File doesn't exist'
            print("File doesn't exist")

    @content.setter
    def content(self, value):
        # попытка записи в файл указанного содержимого
        with open(self.filepath,'w') as f:
            return f.write(value)

    @content.deleter
    def content(self):
        # удаляем файл: os.remove(имя_файла)
        os.remove(self.filepath)


wstf = WrapStrToFile()
print(wstf.content)  # Output: File doesn't exist
wstf.content = 'test str'
print(wstf.content)  # Output: test_str
wstf.content = 'text 2'
print(wstf.content)  # Output: text 2
del wstf.content  # после этого файла не существует
