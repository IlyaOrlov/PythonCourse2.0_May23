def remove_column(matrix, digit):
    num_columns = len(matrix[0])
    indices_to_remove = set()
    for i in range(num_columns):
        if any(row[i] == digit for row in matrix):
            indices_to_remove.add(i)
    new_matrix = []
    for row in matrix:
        new_row = [row[i] for i in range(num_columns) if i not in indices_to_remove]
        new_matrix.append(new_row)
    return new_matrix

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

new_matrix = remove_column(matrix, 3)

for row in new_matrix:
    print(row)
'''
тип контейнера set для indices_to_remove, что позволяет эффективно проверять наличие индексов во множестве с помощью оператора
in. Это обеспечивает более быструю и оптимальную проверку наличия индексов столбцов для удаления.
'''