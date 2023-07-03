def remove_column(matrix, digit):
    num_columns = len(matrix[0])
    indices_to_remove = []
    for i in range(num_columns):
        has_digit = False
        for row in matrix:
            if row[i] == digit:
                has_digit = True
                break
        if has_digit:
            indices_to_remove.append(i)
    new_matrix = []
    for row in matrix:
        new_row = [row[i] for i in range(num_columns) if i not in indices_to_remove]
        new_matrix.append(new_row)
    return new_matrix

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

new_matrix = remove_column(matrix, 5)

for row in new_matrix:
    print(row)