import random

srt = input("Сделайте выбор: камень, ножницы , бумага?   ")
lst = ["камень" , "ножницы" , "бумага"]
x = random.choices(lst, k=1)[0]
print(f'Я загадал {x}')
if srt == x:
    print("Ничья")
elif srt == "камень" and x == "ножницы":
    print("Ты выиграл")
elif srt == "камень" and x == "бумага":
    print("Ты проиграл")
elif srt == "ножницы" and x == "бумага":
    print("Ты выиграл")
elif srt == "ножницы" and x == "камень":
    print("Ты проиграл")
elif srt == "бумага" and x == "камень":
    print("Ты выиграл")
elif srt == "бумага" and x == "ножницы":
    print("Ты проиграл")
else:
    print("Некорретно введено слово")


