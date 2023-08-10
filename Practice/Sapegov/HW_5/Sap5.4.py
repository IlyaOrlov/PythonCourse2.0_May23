def deleter(lst, del_el):
    for i in lst:
        j = 0
        while j < len(i):
            if i[j] != del_el:
                j += 1
            else:
                x = 0
                while x < len(lst):
                    del lst[x][j]
                    x += 1
    return lst


matrix1 = [[1, 3, 44, 5], [5, 4, 5, 7], [1, 7, 6, 7], [53, 3, 2, 5]]
number1 = 5
matrix2 = [[1, 2, 2], [1, 1, 1]]
number2 = 2
print(deleter(matrix1, number1))
print(deleter(matrix2, number2))
