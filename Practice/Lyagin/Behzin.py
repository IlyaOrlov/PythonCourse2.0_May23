start = input("Топлива было: "); end = input("Топлива осталось: ")
distance = input("Расстояние: ")
diff = int(start) - int(end)
# distance было str - сделал число
result = diff / int(distance)
print(f"Расход бензина: {result}")
