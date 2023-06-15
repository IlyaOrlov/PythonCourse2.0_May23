import random


def fun_del(matrix, num):
    ind_del = set()
    for x in matrix:
        for index, j in enumerate(x):
            if j == num:
                ind_del.add(index)
    ind_del = list(ind_del)
    ind_del.sort(reverse=True)  # Сортировка в обратном порядке
    for index, x in enumerate(matrix):
        for index2 in ind_del:
            matrix[index].pop(index2)
    return matrix


m = int(input("Введите размерность матрицы: "))
n = int(input("Введите размерность матрицы: "))
matrix = [[random.randint(1, 11) for j in range(n)] for i in range(m)]
# matrix = [[1, 2, 3], [1, 2, 0], [1, 2, 10]]
print(f"Исходная матрица: {matrix}")
num = int(input("Число которое вы хотели бы удалить: "))
print(f"Новая матрица: {fun_del(matrix, num)}")
