# Есть список списков (матрица).
# Каждый внутренний список – это строка матрицы.
# Необходимо реализовать функцию, которая удаляет столбец, который содержит заданную цифру.

def del_column(matrix, num):
    del_col = []
    for i in matrix:
        for index, j in enumerate(i):
            if j == num and index not in del_col:
                del_col.append(index)
    del_col.sort()
    for index, i in enumerate(matrix):
        for index2, j in enumerate(del_col):
            matrix[index].pop(j-index2)
    return matrix


matrix = [[1, 2, 3], [4, 2, 333], [1, 3, 2]]
print(f"Ваша матрица: {matrix}")
num = int(input("Введите, число которое требуется удалить: "))
print(f"Полученная матрица: {del_column(matrix, num)}")
