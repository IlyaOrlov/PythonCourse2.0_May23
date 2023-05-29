import random

srt = input("Сделайте выбор: камень, ножницы , бумага?   ").lower()
lst = ["камень" , "ножницы" , "бумага"]
x = random.choice(lst)
print(f'Я загадал {x}')
if srt == x:
    print("Ничья")
elif srt == "камень":
    if x == "ножницы":
        print("Ты выиграл")
    else:
        print("Ты проиграл")
elif srt == "ножницы":
    if x == "бумага":
        print("Ты выиграл")
    else:
        print("Ты проиграл")
elif srt == "бумага":
    if x == "камень":
        print("Ты выиграл")
    else:
        print("Ты проиграл")
else:
    print("Некорретно введено слово")


