start = int(input("Топлива было: "))
end = int(input("Топлива осталось: "))
distance = int(input("Расстояние: "))
diff = start - end
result = diff / distance
print(f'Расход бензина: {result}')