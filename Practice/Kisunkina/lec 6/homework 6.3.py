# Написать класс WrapStrToFIle, который будет иметь одно вычисляемое свойство (property)
# под названием content. В конструкторе класс должен инициализовать атрибут filepath, путем
# присваивания результата функции mktemp библиотеки tempfile. При попытке чтения свойства content
# должен внутри кода свойства открываться файл, используя атрибут filepath
# (с помощью функции open, из этого файла читается все содержимое и возвращается из свойства.
# Если файл не существует, то возникает ошибка, поэтому должна быть обертка вокруг открытия файла
# на чтение (try...except), с помощью которого будет возвращаться 'Файл еще не существует'.
# При присваивании значения свойству content файл по указанному пути должен открываться на запись
# и записываться содержимое. Не забудьте закрывать файл после чтения или записи. При удалении атрибута
# content, должен удаляться и файл.*

import os
import tempfile


class WrapStrToFile:
    def __init__(self):
        self.filepath = tempfile.mktemp()

    @property
    def content(self):
        try:
            with open(self.filepath, "r") as file:
                return file.read()
        except FileNotFoundError:
            return "Файл ещё не существует"

    @content.setter
    def content(self, value):
        with open(self.filepath, "w") as file:
            file.write(value)

    @content.deleter
    def content(self):
        os.remove(self.filepath)


wstf = WrapStrToFile()
print(wstf.content)
wstf.content = "test str"
print(wstf.content)
wstf.content = "text 2"
print(wstf.content)
del wstf.content
