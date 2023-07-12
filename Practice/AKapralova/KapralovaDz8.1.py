# Реализовать итератор, который бы "читал" заданный текст по параграфам.
# Символ параграфа задается отдельно.
class ParagraphIterator:

    def __init__(self, text, paragraph_symbol):
        self.text = text
        self.paragraph_symbol = paragraph_symbol
        self.current_paragraph = 0

    def __iter__(self):
        return self

    def __next__(self):
        res = ''
        if self.current_paragraph > len(self.text) - 1:
            raise StopIteration
        while self.text[self.current_paragraph] != self.paragraph_symbol:
            res += self.text[self.current_paragraph]
            self.current_paragraph += 1
            if self.current_paragraph >= len(self.text):
                break
        else:
            self.current_paragraph += 1
        return res


text = "Дама сдавала в багаж: Диван. Чемодан. Саквояж. Картину. Корзину. Картонку. И маленькую собачонку."

for i in ParagraphIterator(text, "."):
    print(i)
