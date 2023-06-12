def deleter(lst, del_el):
    for i in lst:
        for index2, j in enumerate(i):
            if j == del_el:
                x = 0
                while x < len(lst):
                    del lst[x][index2]
                    x += 1
    return lst


matrix = [[1, 3, 44, 5], [5, 4, 5, 7], [1, 7, 6, 7], [53, 3, 2, 5]]
number = 5
print(deleter(matrix, number))
