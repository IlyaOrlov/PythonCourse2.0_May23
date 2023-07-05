#  Реализовать итератор, который бы "читал" заданный текст по параграфам. Символ параграфа задается отдельно.
class MyClass:

    def __init__(self, text):
        self._obj = MyIter(text)

    def __iter__(self):
        return self._obj


class MyIter:
    __par = '\u00a7'

    def __init__(self, text):
        self._text = text
        self._i = 0

    def __next__(self):
        if self._i < len(self._text) and self._i != -1:
            j = self._text.find(self.__par, self._i + 1)
            if j != -1:
                res = self._text[self._i:j - 1]
            else:
                res = self._text[self._i:]
            self._i = j
            return res
        else:
            raise StopIteration


str1 = '§Мороз и солнце; день чудесный!\nЕще ты дремлешь, друг прелестный —\nПора, красавица, проснись:'\
    '\nОткрой сомкнуты негой взоры\nНавстречу северной Авроры,\nЗвездою севера явись!'\
    '§Вечор, ты помнишь, вьюга злилась,\nНа мутном небе мгла носилась;\nЛуна, как бледное пятно,'\
    '\nСквозь тучи мрачные желтела,\nИ ты печальная сидела —\nА нынче… погляди в окно:'\
    '§Под голубыми небесами\nВеликолепными коврами,\nБлестя на солнце, снег лежит;\nПрозрачный лес один чернеет,'\
    '\nИ ель сквозь иней зеленеет,\nИ речка подо льдом блестит.'

for i in MyClass(str1):
    print(i)
