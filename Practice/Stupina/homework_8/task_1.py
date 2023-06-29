class MyIter:
    __p = '\u00a7'

    def __init__(self, text):
        self._text = text
        self._i = self._text.find(self.__p, 0)
        self.__s_ex = 'Символ не найден'

    def __iter__(self):
        return self

    def __next__(self):
        if self._i != -1:
            j = self._text.find(self.__p, self._i + 1)
            if j != -1:
                res = self._text[self._i:j - 1]
            else:
                res = self._text[self._i:]
                self.__s_ex = 'Конец текста'
            self._i = j
            return res
        else:
            pass
            raise StopIteration(self.__s_ex)


s = '§Зайка\nЗайку бросила хозяйка -\nПод дождем остался зайка.\nСо скамейки слезть не смог,\nВесь до ниточки промок.' \
   '\n§Бычок\nИдет бычок, качается,\nВздыхает на ходу:\n- Ох, доска кончается,\nСейчас я упаду' \
   '\n§Лошадка\nЯ люблю свою лошадку,\nПричешу ей шерстку гладко,\nГребешком приглажу хвостик\nИ верхом поеду в гости'

for i in MyIter(s):
    print(i)
