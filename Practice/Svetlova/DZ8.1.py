class ParagraphIterator:
    def __init__(self, text, paragraph_symbol):
        self.paragraphs = iter(text.split(paragraph_symbol))

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.paragraphs)

# Пример использования

text = "Это первый параграф.§Это второй параграф.§Это третий параграф. "
paragraph_symbol = "§"

paragraph_iterator = ParagraphIterator(text, paragraph_symbol)

for paragraph in paragraph_iterator:
    print(paragraph)