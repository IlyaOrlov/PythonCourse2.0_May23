import random

lst = ["Ты хоть понял что написал?", "Аргументируй", "И?"]
x = 0
while not (input(f"{lst[x]} \n :")).lower() == "хватит":
    x += 1
    if x > 2:
        x = 0

print("Фу сдался")
