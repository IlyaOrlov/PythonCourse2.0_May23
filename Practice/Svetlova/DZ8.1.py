class ParagraphIterator:
    def __init__(self, text, paragraph_symbol):
        self.text = text
        self.paragraph_symbol = paragraph_symbol
        self.start = 0
        self.end = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.end >= len(self.text):
            raise StopIteration

        self.start = self.end
        self.end = self.text.find(self.paragraph_symbol, self.start + 1)
        if self.end == -1:
            self.end = len(self.text)

        paragraph = self.text[self.start:self.end].strip(self.paragraph_symbol)
        return paragraph


# Пример использования
text = "Это первый параграф.§Это второй параграф.§Это третий параграф."
paragraph_symbol = "§"

paragraph_iterator = ParagraphIterator(text, paragraph_symbol)

for paragraph in paragraph_iterator:
    print(paragraph)