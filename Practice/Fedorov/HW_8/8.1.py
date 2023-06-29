class Paragraph:

    def __init__(self, txt, simvol):
        self._i = 0
        self._j = 0
        self.txt = txt
        self.simvol = simvol

    def __iter__(self):
        return self

    def __next__(self):
        if self._i < len(self.txt):
            if self.txt[self._i] == self.simvol:
                res = self.txt[self._j:self._i + 1]
                self._j = self._i + 1
                self._i += 1
                return res
            self._i += 1
        else:
            if self._j == 0:
                raise StopIteration
            else:
                res = self.txt[self._j:]
                self._j = 0
                return res


text = "Много дней грустил король; Не знал народ, что за беда; И кто-то во дворец привел;" \
       "Смешного карлика-шута; Карлик прыгал и кричал; Народ безумно хохотал; А шут смешить не прекращал;" \
       "На пол вдруг король упал;"


for element in Paragraph(text, ";"):
    if element:
        print(element)
