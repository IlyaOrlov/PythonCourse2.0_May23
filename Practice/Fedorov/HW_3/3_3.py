

def isnum(t):
    while not (num := input(f"{t}")).isnumeric():
            print(f"Ошибка! {num} - не является числом")
    return num


print("Вы хотите зашифровать или расшифровать пароль?")
while not (x := input("Введите 1 чтобы зашифровать, другая цифра запустит программу расшифровки :2")).isnumeric():
    print(f"Ошибка! {x} - не похоже на 1 или 2")

psw = isnum("Введите пароль или зашифрованный пароль (цифровой): ")
key = isnum("Введите секретный ключ (цифровой): ")
y = int(psw) ^ int(key)
if x == "1":
    print(f"Пароль зашифрован: {y}")
else:
    print(f"Пароль расшифрован: {y}")
