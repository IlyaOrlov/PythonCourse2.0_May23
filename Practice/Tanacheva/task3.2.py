t = float(input("Введите время пути автомобиля в часах:"))
distance = float(input(f"Введите расстояние в километрах, пройденное автомобилем за время {t} часов:"))

speed = round(distance/t, 2)
print(f"Средняя скорость автомобиля равна: {speed} км/ч")
