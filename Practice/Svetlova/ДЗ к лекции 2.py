import math


def square(r):
    return math.pi * r ** 2


radius = input("Введите радиус: ")
result = square(int(radius))
print(f"Площадь круга: {result}")


start = input("Топлива было: ")
end = input("Топлива осталось: ")
distance = int(input("Расстояние: "))
diff = int(start) - int(end)
result = diff / distance
print(f"Расход бензина: {result}")