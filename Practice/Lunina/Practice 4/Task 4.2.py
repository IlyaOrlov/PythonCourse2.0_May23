# 1 часть.Если длина строки не ровна 5 или это не число, то выводить ошибку
while len(a := input("Введите пятизначное число: ")) != 5 or not a.isdigit():
    print(f"Ошибка! {a} - это не пятизначное число или это не число.")

# 2 часть. Если все соблюдено то выдаем число и дальше используем цикл for чтобы разобрать
# последовательность
else:
    print(f"Число: {a}")
    i = 1
    for elem in a:
        print(f" {i} Цифра равна {elem}")
        i += 1

# Рабочий код с while
#i = 0
#while i < 5:
#    print(f" {i + 1} цифра равна {a[i]}")
#    i += 1