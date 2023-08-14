class ParagraphIterator:
    def __init__(self, text, paragraph_symbol):
        self.paragraphs = text.split(paragraph_symbol)  # Разделение текста на параграфы
        self.current_paragraph = 0  # Индекс текущего параграфа

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_paragraph < len(self.paragraphs):
            p = self.paragraphs[self.current_paragraph]
            self.current_paragraph += 1
            return p
        else:
            raise StopIteration


# Тестирование итератора
tx = "Параграф 1. Содержимое параграфа 1. Параграф 2. Содержимое параграфа 2. Параграф 3. Содержимое параграфа 3."
paragraph_sym = "."

iterator = ParagraphIterator(tx, paragraph_sym)
for paragraph in iterator:
    print(paragraph)
