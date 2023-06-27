class MyIter:
    _p = '\u00a7'

    def __init__(self, text):
        self._text = text
        self.i = self._text.find(self._p, 0)
        self.s_ex = 'Символ не найден'

    def __iter__(self):
        return self

    def __next__(self):
        if self.i != -1:
            j = self._text.find(self._p, self.i + 1)
            if j != -1:
                res = self._text[self.i:j - 1]
            else:
                res = self._text[self.i:]
                self.s_ex = 'Конец текста'
            self.i = j
            return res
        else:
            raise StopIteration(self.s_ex)


s = '§Зайка\nЗайку бросила хозяйка -\nПод дождем остался зайка.\nСо скамейки слезть не смог,\nВесь до ниточки промок.' \
   '\n§Бычок\nИдет бычок, качается,\nВздыхает на ходу:\n- Ох, доска кончается,\nСейчас я упаду' \
   '\n§Лошадка\nЯ люблю свою лошадку,\nПричешу ей шерстку гладко,\nГребешком приглажу хвостик\nИ верхом поеду в гости'

ob = MyIter(s)
it = iter(ob)
while True:
    try:
        print(next(it))
        print('------')
    except StopIteration as ex:
        print(ex)
        break
