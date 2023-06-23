def trans_matrix_fun(matrix):
    # транспонируем матрицу
    trans_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return trans_matrix


def del_column(m, n):
    m = trans_matrix_fun(m)
    i = 0
    while i < len(m):
        j = 0
        while j < len(m[i]):
            if m[i][j] == n:
                del (m[i])
                i = 0
                j = 0
            else:
                j += 1
        i += 1
    m = trans_matrix_fun(m)
    return m


matrix = [[4, 2, 3], [4, 4, 6], [7, 8, 9], [4, 7, 90]]
number = int(input("Введите число для удаления:"))
matrix = del_column(matrix, number)
print(matrix)
