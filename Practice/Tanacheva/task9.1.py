class Paragragh:

    def __init__(self, text, symbol):
        self._i = 0
        self._text = text
        self.symbol = symbol

    def __iter__(self):
        return self

    def __next__(self):
        res = ""
        if self._i > len(self._text)-1:
            raise StopIteration
        while self._text[self._i] != self.symbol:
            res += self._text[self._i]
            self._i += 1
            if self._i >= len(self._text):
                break
        else:
            self._i += 1
        return res


text1 = "gsgs;dgssgsgssg;ssdgs;dsdgdsgfd;  ;    dbd"
for i in Paragragh(text1, ";"):
    print(i)
