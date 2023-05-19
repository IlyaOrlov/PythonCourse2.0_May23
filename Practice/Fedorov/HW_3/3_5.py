txt = input("Привет! Введи слово, фразу или чиcло, а я скажу палиндром это или нет: ")


def preobrazovanie(x):
    x = x.lower()
    x = x.replace(" ", "")
    return x


txt = preobrazovanie(txt)
if txt == txt[::-1]:
    print("Это палиндром!")
else:
    print("Не похоже на палиндром :)")
