# Реализовать итератор, который бы "читал" заданный текст по параграфам. Символ параграфа задается отдельно.
class ReadPar:
    def __init__(self, text, symbol):
        self._i = 0
        self._s = 0
        self._text = text
        self._symbol = symbol

    def __iter__(self):
        return self

    def __next__(self):
        while self._i < len(self._text):
            if self._text[self._i] == self._symbol:
                res = self._text[self._s: self._i]
                self._s = self._i + 1
                self._i += 1
                return res
            self._i += 1
        else:
            raise StopIteration


text = "Месяц задумчивый, полночь глубокая…|"\
       "Хутор в степи одинок…|"\
       "Дремлет в молчанье равнина широкая,|"\
       "Тепел ночной ветерок.|"\
       "(И. Бунин - Месяц  задумчивый…)|"

for elm in ReadPar(text, "|"):
    if elm:
        print(elm)
