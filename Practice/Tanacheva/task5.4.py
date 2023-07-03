def trans_matrix_fun(matrix):
    # транспонируем матрицу
    trans_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return trans_matrix


def del_column(m, n):
    m = trans_matrix_fun(m)
    i = 0
    while i < len(m):
        if n in m[i]:
            del m[i]
        else:
            i += 1
    if m != []:
        m = trans_matrix_fun(m)
    return m


matrix = [[4, 4], [4, 3]]
number = int(input("Введите число для удаления:"))

matrix = del_column(matrix, number)
print(matrix)
