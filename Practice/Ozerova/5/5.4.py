def del_col(x, y):
    for i in x:
        j = 0
        while j < len(i):
            if i[j] != y:
                j += 1
            else:
                a = 0
                while a < len(x):
                    del x[a][j]
                    a += 1
    return x

arr = [[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 10]]
number = 4
print(del_col(arr, number))
