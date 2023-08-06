# Есть список списков (матрица). Каждый внутренний список – это строка матрицы.
# Необходимо реализовать функцию, которая удаляет столбец, который содержит заданную цифру.

import random


def search_columns(matrix):
    number = int(input("Введите число от 0 до 10"
                       " Столбец, содержащий заданную цифру будет удалён из матрицы: "))
    arr = set()
    for line in matrix:
        for _id, elem in enumerate(line):
            if elem == number:
                arr.add(_id)
    return arr


def del_columns(matrix, arr):
    for _id in reversed(sorted(arr)):
        for line in matrix:
            del line[_id]
    print ("Получившаяся матрица: ")
    for i in range(lines):
        print(matrix[i])


if __name__ == '__main__':
    lines = int(input("Количество строк в матрице: "))
    columns = int(input("Количество столбцов в матрице: "))
    matrix = [[random.randint(0, 10) for j in range(columns)] for i in range(lines)]
    print('-------------------------')
    print("Получилась такая матрица:")
    for i in range(lines):
        print(matrix[i])
    arr = search_columns(matrix)
    del_columns(matrix, arr)


