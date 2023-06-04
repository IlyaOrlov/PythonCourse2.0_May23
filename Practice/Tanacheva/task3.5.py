word1 = input("Введите слово для проверки: ")
word1 = word1.lower()
word2 = word1[::-1]
print(f"Слово является палиндромом? {word2 == word1}")
