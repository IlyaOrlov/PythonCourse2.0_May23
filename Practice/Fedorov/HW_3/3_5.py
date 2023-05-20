

def preobrazovanie(x):
    x = x.lower().replace(" ", "")
    return x


txt = input("Привет! Введи слово, фразу или чиcло, а я скажу палиндром это или нет: ")
txt = preobrazovanie(txt)
if txt == txt[::-1]:
    print("Это палиндром!")
else:
    print("Не похоже на палиндром :)")
