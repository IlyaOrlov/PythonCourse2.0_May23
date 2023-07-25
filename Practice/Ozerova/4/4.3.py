x = ""
while (y := input("Ввведите число: ").upper()) != "STOP":
    if not y.isdecimal():
        print("Необходимо ввести число: ")
    else:
        x += y
else:
    print(x)
