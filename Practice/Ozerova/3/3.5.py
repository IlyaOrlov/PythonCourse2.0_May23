x = input("Введите слово:")
x = x.lower()
if x == x[::-1]:
    print("Это слово является палиндромом")
else:
    print("Это слово не является палиндромом")
