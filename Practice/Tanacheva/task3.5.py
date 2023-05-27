word1 = str(input("Введите слово для проверки: "))
word2 = word1.lower()[::-1]
print (f"Слово является палиндромом? {word2 == word1.lower()}")
