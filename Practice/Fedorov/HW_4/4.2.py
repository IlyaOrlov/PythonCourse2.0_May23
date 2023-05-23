while not ((x := input("Введите целое пятизначное число: ")).isnumeric() and len(x) == 5):
    print(f"{x} -  это не целое пятизначное число.")

for index, i in enumerate(x):
    print(f"{index + 1} цифра равна {x[index]}")
