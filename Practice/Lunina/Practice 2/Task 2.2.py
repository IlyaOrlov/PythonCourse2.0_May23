start = input("Топлива было: ")
#  Каждую функцию лучше писать в отдельной строке. Исправлено
end = input("Топлива осталось: ")
distance = input("Расстояние: ")
diff = int(start) - int(end)
# Py "distance"  видит как строку. Исправлено на число
result = diff / int(distance)
print(f"Расход бензина: {result}")
