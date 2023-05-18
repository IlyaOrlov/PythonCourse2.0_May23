# Найти и исправить ошибки в программе
# Ошибка была на 6 строке, т.е. diff - это число, а distance- строка
# Решение - преобразовать входные данные переменной distance в число с помощью int(input())
start = input("Топлива было: "); end = input("Топлива осталось: ")
distance = int(input("Расстояние: "))
diff = int(start) - int(end)
result = diff / distance
print(f"Расход бензина: {result}")
