def transp(arr):
    arr_trans = [[0 for j in range(len(arr))] for i in range(len(arr[0]))]
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            arr_trans[j][i] = arr[i][j]
    return arr_trans


def del_column(arr,a):
    delindex = set()
    for index, i in enumerate(arr):
        for index1, j in enumerate(i):
            if j == a:
                if index1 not in delindex:
                    delindex.add(index1)
    delindex = list(delindex)
    delindex.sort(reverse=True)
    arr = transp(arr)
    for i in delindex:
        del arr[i]
    arr = transp(arr)
    return print(arr)


matrix = [[9,2,5],[4,5,5],[7,8,9]]
del_column(matrix,5)