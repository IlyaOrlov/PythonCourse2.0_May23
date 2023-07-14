class Paragraph:

    def __init__(self, text, par):
        self.text = text
        self.par = par
        self.x = 0
    def __iter__(self):
        return self

    def __next__(self):
        res = ''
        if self.x > len(self.text) - 1:
            raise StopIteration
        while self.text[self.x] != self.par:
            res += self.text[self.x]
            self.x += 1
            if self.x >= len(self.text):
                break
        else:
            self.x += 1
        return res


y = "&Здесь начинается первый параграф &Здесь начинается второй параграф"

for i in Paragraph(y, "&"):
    if i:
        print(i)
