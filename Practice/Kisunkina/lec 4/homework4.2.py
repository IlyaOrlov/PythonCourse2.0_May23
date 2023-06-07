len_str = 5
i = 0

while True:
    number = input("Введите пятизначное число: ")
    if len(number) == len_str:
        while i < 5:
            print(f"{i+1} цифра равна {number[i]}")
            i += 1
        break
    else:
        len(number) != len_str
        print(f"Введена неверная длина строки, введите {len_str}-значное число")
