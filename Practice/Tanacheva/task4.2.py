s = input("Введите пятизначное число:")

for number in range(0, len(s)):
    print(f"{number+1} цифра равна {s[number]}")
