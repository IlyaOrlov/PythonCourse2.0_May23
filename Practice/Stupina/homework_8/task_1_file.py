import os.path


class MyIter:
    __p = '§'

    def __init__(self, name_file):
        if os.path.exists(name_file):
            self.__f = open(name_file, encoding='utf-8')
        else:
            raise FileNotFoundError
        self.__s = self.__f.read(1)

    def __iter__(self):
        return self

    def __next__(self):
        res = ''
        while self.__s != self.__p:
            if self.__s == '':
                raise StopIteration
            self.__s = self.__f.read(1)
        res += self.__s
        self.__s = self.__f.read(1)
        while self.__s != self.__p and self.__s != '':
            res += self.__s
            self.__s = self.__f.read(1)
        return res

    def __del__(self):
        if hasattr(self, '_MyIter__f'):
            self.__f.close()
            print('Файл закрыт')


for i in MyIter('task_1text.txt'):
    print(i)
    print('---')
