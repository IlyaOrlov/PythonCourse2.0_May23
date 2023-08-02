def remove_column(m, d):
    x = len(m)
    y = len(m[0]) if x > 0 else 0
    z = []
    for i in range(y):
        for j in range(x):
            if m[j][i] == d:
                z.append(i)
                break
    for j in m:
        for i_index in sorted(z, reverse=True):
            del j[i_index]
    return m


my_m = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 0, 1, 2]
]

print(my_m)
b = int(input("Будет удален столбец с цифрой: "))
result = remove_column(my_m, b)
print(result)
