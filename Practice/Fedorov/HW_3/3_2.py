print("Привет Эта мини программа, создана для расчета средней скорости автомобиля")


# Проверка верно введенных данных Скорости и Расстояния
def isnum(t):
    x = "Текст"
    while not x.replace(".", "").isnumeric():
        x = input(f"Введите {t}")
        if not x.replace(".", "").isnumeric():
            print(f"Ошибка! {x} - не является числом")
    return x


a = isnum("расстояние, которое вы проехали(км): ")
b = isnum("время в пути в часах: ")
kmInHour = float(a) / float(b)
print(f"Срядняя скорость была равна = {kmInHour} км/ч")
