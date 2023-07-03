def remove_column(m, d):
    for row in m:
        if d in row:
            column_index = row.index(d)
            for i in range(len(m)):
                del m[i][column_index]
            return m
    return m


my_m = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(my_m)
b = int(input("Будет удален столбец с цифрой: "))
result = remove_column(my_m, b)
print(result)
