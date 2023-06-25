def remove_column(m, d):
    num_columns = len(m[0])
    new_matrix = [[row[i] for i in range(num_columns) if row[i] != d] for row in m]
    return new_matrix


my_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
digit_to_remove = 2

result_matrix = remove_column(my_matrix, digit_to_remove)
print("Матрица после удаления столбца с цифрой", digit_to_remove)
for row in result_matrix:
    print(row)
