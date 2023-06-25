import tempfile
import os


class WrapStrToFile:
    def __init__(self):
        self.filepath = tempfile.mktemp()

    @property
    def content(self):
        try:
            with open(self.filepath) as f:
                return f.read()
        except FileNotFoundError:
            return 'Файл еще не существует!'

    @content.setter
    def content(self, value):
        with open(self.filepath, 'w') as f:
            f.write(value)

    @content.deleter
    def content(self):
        os.remove(self.filepath)


wstf = WrapStrToFile()
print(wstf.content)  # Output: File doesn't exist
wstf.content = 'test str'
print(wstf.content)  # Output: test_str
wstf.content = 'text 2'
print(wstf.content)  # Output: text 2
del wstf.content
