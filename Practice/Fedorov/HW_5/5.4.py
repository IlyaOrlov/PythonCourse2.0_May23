# Есть список списков (матрица).
# Каждый внутренний список – это строка матрицы.
# Необходимо реализовать функцию, которая удаляет столбец, который содержит заданную цифру.

def del_column(matrix, num):
    del_col = set()
    for i in matrix:
        for index, j in enumerate(i):
            if j == num:
                del_col.add(index)
    del_col = list(del_col)
    del_col.sort(reverse=True)
    for index, i in enumerate(matrix):
        for index2 in del_col:
            matrix[index].pop(index2)
    return matrix


matrix = [[1, 2, 3], [4, 2, 333], [1, 3, 2]]
print(f"Ваша матрица: {matrix}")
num = int(input("Введите, число которое требуется удалить: "))
print(f"Полученная матрица: {del_column(matrix, num)}")
