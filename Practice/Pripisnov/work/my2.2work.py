start = int(input("Топлива было: "))
end = int(input("Топлива осталось: "))
distance = int(input("Расстояние: "))
diff = start - end
result = distance / diff
print(f"Расход бензина: {result}")
