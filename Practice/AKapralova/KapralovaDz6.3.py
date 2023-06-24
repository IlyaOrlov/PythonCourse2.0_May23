import os
import tempfile


class WrapStrToFile:
    def __init__(self):
        self.filepath = tempfile.mktemp()

    @property
    def content(self):
        try:
            with open(self.filepath) as my_file:
                s = my_file.read()
            return s
        except:
            return "File doesn't exist"

    @content.setter
    def content(self, value):
        with open(self.filepath, "w") as my_file:
            my_file.write(value)

    @content.deleter
    def content(self):
        os.remove(self.filepath)


wstf = WrapStrToFile()
print(wstf.content)
wstf.content = 'test str'
print(wstf.content)
wstf.content = 'text 2'
print(wstf.content)
del wstf.content
print(wstf.content)
