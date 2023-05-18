print("Вы хотите зашифровать или расшифровать пароль?")


def isnum(t):
    num = "Текст"
    while not num.isnumeric():
        num = input(f"{t}")
        if not num.isnumeric():
            print(f"Ошибка! {num} - не является числом")
    return num


x = "Текст"
while not (x == "1" or x == "2"):
    x = input("Введите 1 - зашифровать или 2 - расшифровать: ")
    if not (x == "1" or x == "2"):
        print(f"Ошибка! {x} - не похоже на 1 или 2")

psw = isnum("Введите пароль или зашифрованный пароль (цифровой): ")
key = isnum("Введите секретный ключ (цифровой): ")
y = int(psw) ^ int(key)
if x == "1":
    print(f"Пароль зашифрован: {y}")
else:
    print(f"Пароль расшифрован: {y}")
