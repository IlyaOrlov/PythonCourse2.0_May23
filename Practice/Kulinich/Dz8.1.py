class Reader:
    def __init__(self, txt, smb):
        self.txt = txt
        self.smb = smb
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        res = ''
        if self.i < len(self.txt):
            while self.txt[self.i] != self.smb:
                res += self.txt[self.i]
                self.i += 1
                if self.i >= len(self.txt):
                    break
            self.i += 1
        else:
            raise StopIteration
        return res


txt = "1q&2w&3e"
paragraph = Reader(txt, '&')

for i in paragraph:
    print(i)