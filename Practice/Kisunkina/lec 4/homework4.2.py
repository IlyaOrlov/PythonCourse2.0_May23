len_str = 5

while True:
    number = input(f"Введите {len_str}-значное число: ")
    if len(number) == len_str:
        i = 0
        while i < 5:
            print(f"{i+1} цифра равна {number[i]}")
            i += 1
        break
    else:
        print(f"Введена неверная длина строки, введите {len_str}-значное число")
