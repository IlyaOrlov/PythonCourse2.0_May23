txt = input("Привет! Введи слово фразу или чиcло, а я скажу палиндром это или нет: ")


def preobrazovanie(self):
    self = self.lower()
    self = self.replace(" ", "")
    return self


txt = preobrazovanie(txt)
if txt == txt[::-1]:
    print("Это палиндром!")
else:
    print("Не похоже на палиндром :)")
