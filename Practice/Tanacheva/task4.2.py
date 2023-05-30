s = str(input("Введите пятизначное число:"))

for number in range(0, 5):
    print(f"{number+1} цифра равна {s[number]}")
