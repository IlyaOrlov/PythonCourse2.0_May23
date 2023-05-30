# Найти первую цифру в строке, введённой пользователем
def find_decimal(s):
    for i in s:
        if i.isdecimal():
            print(f"Искомый символ - {i}")
            break
    else:
        print("Ничего не найдено!")


# s = input("Введите строку: ")
find_decimal("akkdd3rrr4")
find_decimal("aaaaaddd")
find_decimal("4444444")

