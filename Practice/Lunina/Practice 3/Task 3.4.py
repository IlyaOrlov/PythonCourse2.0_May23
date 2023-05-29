import time


print("Добрый день! Давай чуть-чуть похулиганим.")
time.sleep(2)

language = input("Будем вести беседу на русском?: ")
if language.upper() == "ДА":
    a = input("Введите фразу на русском языке с буквой 'а': ")
    a1 = a.replace("а", "*")
    print(a1)
    b = input("напиши еще что-нибудь с буквой 'а': ")
    b1 = b.replace("а", "*")
    print(b1)
    time.sleep(2)
if language.upper() == "LF":
    c = input("Введите фразу на русском языке с буквой 'а': ")
    c1 = c.replace("а", "*")
    print(c1)
    d = input("напиши еще что-нибудь с буквой 'а': ")
    d1 = d.replace("а", "*")
    print(d1)
    time.sleep(2)
if language.upper() == "НЕТ":
    e = input("Введите фразу на английском языке с буквой 'a': ")
    e1 = e.replace("a", "*")
    f = input("напиши еще что-нибудь с буквой 'a': ")
    f1 = f.replace("a", "*")
    print(f1)
    time.sleep(2)
else:
    print("Вы ничего не ввели. ")

print("С тобой было интересно!Good bay.")
