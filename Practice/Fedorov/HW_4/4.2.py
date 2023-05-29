while not ((x := input("Введите целое пятизначное число: ")).isnumeric() and len(x) == 5):
    print(f"{x} -  это не целое пятизначное число.")

for index, i in enumerate(x, 1):
    print(f"{index} цифра равна {i}")
