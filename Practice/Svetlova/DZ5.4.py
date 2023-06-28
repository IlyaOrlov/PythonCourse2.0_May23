def remove_column(matrix, digit):
    new_matrix = []
    for row in matrix:
        new_row = [elem for elem in row if elem != digit]
        new_matrix.append(new_row)
    return new_matrix

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

new_matrix = remove_column(matrix, 5)

for row in new_matrix:
    print(row)