print("Привет Эта мини программа, создана для расчета периметра прямоугольника")


# Проверка верно введенных данных Длинны и Ширины
def isnum(t):
    x = "Текст"
    while not x.replace(".", "").isnumeric():
        x = input(f"Введите {t} прямоугольника: ")
        if not x.replace(".", "").isnumeric():
            print(f"Ошибка! {x} - не является числом")
    return x


a = isnum("Длину")
b = isnum("Ширину")
perimetrP = (float(a) + float(b)) * 2
print(f"Периметр введенного прямоугольника равен = {perimetrP}")
