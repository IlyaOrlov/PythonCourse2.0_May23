def transp(arr):
    arrTrans = [[0 for j in range(len(arr))] for i in range(len(arr[0]))]
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            arrTrans[j][i] = arr[i][j]
    return arrTrans


def DelColumn(arr,a):
    delindex = []
    for index, i in enumerate(arr):
        for index1, j in enumerate(i):
            if j == a:
                if index1 not in delindex:
                    delindex.append(index1)
    delindex.sort()
    arr = transp(arr)
    for i in range(len(delindex) - 1, -1, -1):
        del arr[delindex[i]]
    arr = transp(arr)
    return print(arr)


matrix = [[9,2,5],[4,5,5],[7,8,9]]
DelColumn(matrix,5)