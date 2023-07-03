class Reader:

    def __init__(self, text, symbol):
        self.text = text
        self.symbol = symbol
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        res = ''
        if self.i > len(self.text) - 1:
            raise StopIteration
        while self.text[self.i] != self.symbol:
            res += self.text[self.i]
            self.i += 1
            if self.i >= len(self.text):
                break
        self.i += 1
        return res


x = "$frtffttf55 dd44d $fgc4 feef$fg5 fdsy"
y = Reader(x, '$')

for i in y:
    print(i)
