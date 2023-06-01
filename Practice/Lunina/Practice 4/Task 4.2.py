while (i :=input("Введите пятизначное число: ")) != "stop":
    if i.isdigit():
        if len(i) == 5:
            print(f" Число: {i}")
            print(f" 1 цифра равна {i[0]}")
            print(f" 2 цифра равна {i[1]}")
            print(f" 3 цифра равна {i[2]}")
            print(f" 4 цифра равна {i[3]}")
            print(f" 5 цифра равна {i[4]}")
            break
        else:
            print("Ошибка. Введите число из 5 цифр")
            continue
    else:
        print("Ошибка. Введите только число")
        continue
